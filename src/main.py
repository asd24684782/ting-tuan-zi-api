# -*- coding: UTF-8 -*-
# Standard library imports
import logging
import time
import os
from datetime import datetime

# Third party imports
from fastapi import  FastAPI

# Local application imports
from schema.schema import *
from routers import festivalRouter
from config.config import DATABASE_HOST

#---------------- global -------------------# 
app = FastAPI()
app.include_router(festivalRouter.router)

logger = logging.getLogger()
logging.basicConfig(level=logging.WARNING,format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')

#---------------- Dependency -------------------# 

#----------------- func -----------------------#

#------------------- api ---------------------#
@app.on_event("startup")
async def startup_event():
    pass
        

@app.get('/api/1.0/ping', tags=["test"])
async def ping():
    data = {
        'message': "pong",
        'time'   : int(time.time() * 1000),
        'now'    : str(datetime.now())
    }
    return data


@app.get('/api/1.0/debug/{debugLevel}', tags=["test"])
async def debug(debugLevel):
    currentLogLevel = logger.level
    code     = "00"
    message  = "Success"
    okset = {'DEBUG':logging.DEBUG,'INFO':logging.INFO,'WARNING':logging.WARNING}
    data = {
        'code' : code,
        'message' : message,
    }

    # get new debug level
    newLevel = debugLevel.upper()
    
    if newLevel in okset:
        levelValue = okset.get(newLevel)
        logger.setLevel(levelValue)

        data['log_level_before'] = f"{currentLogLevel}-{logging.getLevelName(currentLogLevel)}"
        data['log_level_now']    = f"{levelValue}-{logging.getLevelName(levelValue)}"
        data['now']              = str(datetime.now())
    else:
        data['code']    = "01"
        data['message'] = f"Invalid Debug Level. Accaptable Levels:{list(okset)}"

    
    return data


