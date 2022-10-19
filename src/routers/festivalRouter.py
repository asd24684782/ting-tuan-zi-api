# -*- coding: UTF-8 -*-
# Standard library imports
import logging

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
async def readfestivals():
    logger.warning(f'########### get festivals ###########')
    festivals = festivalDB.getFestivals()

    return festivals

@router.post('/')
async def postfestival(festivalBody: festivalPostRequestBody):
    logger.warning(f'########### post festivals ###########')
    code     = "00"
    message  = "Success"

    try:
        logger.debug(festivalBody)
        festivalDB.insertFestival(
            name=festivalBody.name,
            date=festivalBody.date,
            location=festivalBody.location,
            bands=festivalBody.bands
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
        profileDB.deleteProfile(profileUUID)

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