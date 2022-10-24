from tkinter.font import names
from xmlrpc.client import boolean
from pydantic import BaseModel
from typing import List


class festivalPostRequestBody(BaseModel):
    name        : str
    date        : str
    location    : str
    free        : bool
    bands       : List[str]


class festivalSchema(festivalPostRequestBody):
    id          : str


class bandPostRequestBody(BaseModel):
    name       :str
    members    :List[str]
    albums     :List[str] 

class bandSchema(bandPostRequestBody):
    id  :str

class actorPostRequestBody(BaseModel):
    name    :str
    band    :List[str]

class actorSchema(actorPostRequestBody):
    id  :str