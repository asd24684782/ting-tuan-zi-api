from datetime import datetime, timedelta
from typing import Collection
import logging

from fastapi import Depends, FastAPI, HTTPException, status, Request

import time
from db import DB

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')

app = FastAPI()
app.db = DB.getInstance()

@app.middleware("http")
async def add_version_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/user")
def getUsers():
    logger.debug('=======getUsers=======')
    code     = "00"
    message  = "Success"
    try:
        collection = 'users'
        users = app.db.readAll(collection)
        responseBody = {
            'code' : code,
            'message' : message,
            'users' :users
        }
    except:
        code     = "00"             
        message  = "failed"
        responseBody = {
            'code' : code,
            'message' : message,
        }  
    finally:
        return responseBody

@app.get("/user/{account}")
def getUser(account):
    logger.debug('=======getUsers=======')
    code     = "00"
    message  = "Success"
    try:
        collection = 'users'
        users = app.db.read(collection, account)
        responseBody = {
            'code' : code,
            'message' : message,
            'users' :users
        }
    except:
        code     = "00"             
        message  = "failed"
        responseBody = {
            'code' : code,
            'message' : message,
        }  
    finally:
        return responseBody



@app.post("/user")
def postUser(account, password):
    logger.debug('=======postUser=======')
    code     = "00"
    message  = "Success"

    try:
        collection = 'users'
        dataDict = {
            'account' : account,
            'password': password
        }

        app.db.create(collection, dataDict)
        responseBody = {
            'code' : code,
            'message' : message,
        }
    except:
        code     = "00"             
        message  = "failed"
        responseBody = {
            'code' : code,
            'message' : message,
        }  
    finally:
        return responseBody


@app.put("/user")
def putUser(account, password):
    logger.debug('=======putUser=======')
    code     = "00"
    message  = "Success"

    try:
        collection = 'users'
        app.db.update(collection, account, password)
        responseBody = {
            'code' : code,
            'message' : message,
        }
    except:
        code     = "00"             
        message  = "failed"
        responseBody = {
            'code' : code,
            'message' : message,
        }  
    finally:
        return responseBody


@app.delete("/user")
def deleteUser(account):
    logger.debug('=======deleteUser=======')
    code     = "00"
    message  = "Success"

    try:
        collection = 'users'
        app.db.delete(collection, account)
        responseBody = {
            'code' : code,
            'message' : message,
        }
    except:
        code     = "00"             
        message  = "failed"
        responseBody = {
            'code' : code,
            'message' : message,
        }  
    finally:
        return responseBody
