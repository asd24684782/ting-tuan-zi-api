# -*- coding: UTF-8 -*-
# Standard library imports
import logging

# Third party imports
from fastapi import APIRouter, Depends, HTTPException

# Local application imports


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def readUsers():
    pass

@router.get("/{userID}")
async def readUser(userID: str):
    pass