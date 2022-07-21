from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, status, Request

import time
from db import DB


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
def getUser():
    
    return {"message": "pong"}
