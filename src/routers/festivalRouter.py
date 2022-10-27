# -*- coding: UTF-8 -*-
# Standard library imports
import logging
from datetime import date, datetime
# Third party imports
from fastapi import APIRouter

# Local application imports
from model.festival import Festival
from setting.setting import DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, DB_NAME
from schema.schema import festivalPostRequestBody, festivalSchema


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

@router.get("/")
async def readFestivals():
    logger.warning(f'########### get festivals ###########')
    festivals = await festivalDB.getFestivals()

    return festivals

@router.get('/{id}')
async def readFestivalByID(id: int):
    logger.warning(f'############## get festival {id} ################')
    code     = "00"
    message  = "Success"

    try:
        record = await festivalDB.getFestivalByID(id)

        festival =  {
            "id"        :record[0],
            "name"      :record[1],
            "location"  :record[2],
            "bands"     :record[3],
            "free"      :record[4],
            "notes"     :record[5],
            "area"      :record[6],
            "start"     :record[7],
            "end"       :record[8]
        }
 

        data = {
            'code' : code,
            'message' : message,
            'festival': festival
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

@router.put('/')
async def updateFestival(festivalBody: festivalSchema):
    logger.warning(f'########### update festivals ###########')
    code     = "00"
    message  = "Success"

    try:
        logger.debug(festivalBody)

        await festivalDB.updateFestival(
            id=festivalBody.id,
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

@router.delete('/')
async def deleteProfile(profileUUID):
    logger.warning(f'########### delete Profiles by uuid {profileUUID} ###########')
    code     = "00"
    message  = "Success"

    try:
        await profileDB.deleteProfile(profileUUID)

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