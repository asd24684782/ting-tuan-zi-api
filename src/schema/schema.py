from xmlrpc.client import boolean
from pydantic import BaseModel
from typing import List


class festivalPostRequestBody(BaseModel):
    uuid        : str
    name        : str
    date        : str
    location    : str
    bands       : List[str]
    free        : bool


class festivalSchema(festivalPostRequestBody):
    id          : str
