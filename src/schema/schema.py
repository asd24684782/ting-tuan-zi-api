from multiprocessing.heap import Arena
from pydantic import BaseModel
from typing import List, Union
from datetime import datetime

class festivalPostRequestBody(BaseModel):
    name        : str
    start       : str
    end         : str
    area        : str
    location    : str
    free        : str
    bands       : Union[List[str], None] = None
    notes       : Union[str, None] = None


class festivalSchema(festivalPostRequestBody):
    id          : int


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