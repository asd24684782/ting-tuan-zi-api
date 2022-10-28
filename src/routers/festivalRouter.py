# -*- coding: UTF-8 -*-
# Standard library imports
import logging
from datetime import date, datetime
from urllib import response
# Third party imports
from fastapi import APIRouter

# Local application imports
from model.festival import Festival
from setting.setting import DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, DB_NAME
from schema.schema import festivalPostRequestBody, festivalSchema

# -------------------- global -----------------------------------
router = APIRouter(
    prefix="/festivals",
    tags=["festivals"],
    responses={404: {"description": "Not found"}},
)
festivalDB = Festival(host=DB_HOST,
                      user=DB_USER, 
                      password=DB_PASSWORD,
                      port=DB_PORT,
                      dbName=DB_NAME)
logger = logging.getLogger()

# ---------------------- func -----------------------------------

def makeDateStr(start, end):
    dateStr = f'{start} ~ {end}' if start != end else start
    return dateStr

def makeBandStr(bands):
    bandStr = ""
    for band in bands:
        bandStr = bandStr + str(band) + "、"
    bandStr = bandStr[:-1]

    return bandStr

# ----------------------- api ------------------------------------
@router.get("/")
async def readFestivals():
    logger.warning(f'########### get festivals ###########')
    code     = "00"
    message  = "Success"
    try:
        festivals = await festivalDB.getFestivalsIn30day()
        if not festivals:
            raise ValueError('Data not exist')

        response = []
        for f in festivals:
            temp = {
                'id': f[0],
                'name': f[1],
                'date': makeDateStr(f[2], f[3])
            }
            response.append(temp)


        data = {
            'code' : code,
            'message': message,
            'festivals': response
        }


    except ValueError:
        code = '01'
        message = 'no festival in 30 days '
        data = {
            'code': code,
            'message': message
        }

    except:
        code = '01'
        message = 'failed'
        data = {
            'code': code,
            'message': message
        }       

    finally:
        return data

@router.post('/')
async def postFestival(festivalBody: festivalPostRequestBody):
    logger.warning(f'########### post festivals ###########')
    code     = "00"
    message  = "Success"

    try:
        logger.debug(festivalBody)

        await festivalDB.insertFestival(
            name=festivalBody.name,
            start=datetime.strptime(festivalBody.start, '%Y-%m-%d %H:%M:%S'),
            end=datetime.strptime(festivalBody.end, '%Y-%m-%d %H:%M:%S'),
            area=festivalBody.area,
            location=festivalBody.location,
            free=bool(festivalBody.free.lower() == 'true'),
            bands=festivalBody.bands,
            notes=festivalBody.notes
        )

        data = {
            'code' : code,
            'message' : message,
        }

    except:
        code     = "01"
        message  = "failed"
        data = {
            'code' : code,
            'message' : message,
        }

    finally:
        return data

@router.get('/id/{id}')
async def readFestivalByID(id: int):
    logger.warning(f'############## get festival {id} ################')
    code     = "00"
    message  = "Success"

    try:
        festival = await festivalDB.getFestivalByID(id)
        if not festival:
            raise ValueError(f'festival {id} not exist')




        festival =  {
            "id"        : festival[0],
            "name"      : festival[1],
            "location"  : festival[2],
            "bands"     : makeBandStr(festival[3]),
            "pay"       : '免費' if festival[4] else '要錢' ,
            "notes"     : festival[5],
            "area"      : festival[6],
            "date"      : makeDateStr(festival[7], festival[8])
        }
 

        data = {
            'code' : code,
            'message' : message,
            'festival': festival
        }

    except ValueError:
        code = '01'
        message = f'festival {id} not exist'
        data = {
            'code': code,
            'message': message
        }

    except:
        code     = "01"
        message  = "failed"
        data = {
            'code' : code,
            'message' : message,
        }   

    finally:
        return data

@router.put('/id/{id}')
async def updateFestival(id: int, festivalBody: festivalSchema):
    logger.warning(f'########### update festivals {id} ###########')
    code     = "00"
    message  = "Success"

    try:
        logger.debug(festivalBody)

        await festivalDB.updateFestival(
            id=id,
            name=festivalBody.name,
            start=datetime.strptime(festivalBody.start, '%Y-%m-%d %H:%M:%S'),
            end=datetime.strptime(festivalBody.end, '%Y-%m-%d %H:%M:%S'),
            area=festivalBody.area,
            location=festivalBody.location,
            free=bool(festivalBody.free.lower() == 'true'),
            bands=festivalBody.bands,
            notes=festivalBody.notes
        )

        data = {
            'code' : code,
            'message' : message,
        }

    except:
        code     = "01"
        message  = "failed"
        data = {
            'code' : code,
            'message' : message,
        }

    finally:
        return data   

@router.get('/free')
async def readFestivalFree():
    logger.warning(f'############## get festival free ################')
    code     = "00"
    message  = "Success"

    try:
        festivals = await festivalDB.getFestivalFree()
        if not festivals:
            raise ValueError(f'festival free not exist')

        response = []
        for f in festivals:
            temp = {
                'id': f[0],
                'name': f[1],
                'date': makeDateStr(f[2], f[3])
            }
            response.append(temp)


        data = {
            'code' : code,
            'message' : message,
            'festivals': response
        }

    except ValueError:
        code = '01'
        message = f'festival free not exist, 你個免費仔'
        data = {
            'code': code,
            'message': message
        }

    except:
        code     = "01"
        message  = "failed"
        data = {
            'code' : code,
            'message' : message,
        }   

    finally:
        return data

@router.get('/band/{band}')
async def readFestivalByBand(band: str):
    logger.warning(f'############## get festival {band} ################')
    code     = "00"
    message  = "Success"

    try:
        festivals = await festivalDB.getFestivalByBand(band)
        if not festivals:
            raise ValueError(f'festival with {band} not exist')

        response = []
        for f in festivals:
            temp = {
                "id"        : f[0],
                "name"      : f[1],
                "date"      : makeDateStr(f[2], f[3])
            }
            response.append(temp)

        data = {
            'code' : code,
            'message' : message,
            'festivals': response
        }

    except ValueError:
        code = '01'
        message = f'festival with {band} not exist'
        data = {
            'code': code,
            'message': message
        }

    except:
        code     = "01"
        message  = "failed"
        data = {
            'code' : code,
            'message' : message,
        }   

    finally:
        return data