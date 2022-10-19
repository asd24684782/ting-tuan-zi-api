from xmlrpc.client import boolean
from pydantic import BaseModel
from typing import List


class festivalPostRequestBody(BaseModel):
    name        : str
    date        : str
    location    : str
    bands       : List[str]


class festivalSchema(festivalPostRequestBody):
    id          : str
