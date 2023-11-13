from pydantic import BaseModel
from typing import Union
from datetime import datetime


class TypeEntity(BaseModel):
    id: Union[int, None] = None
    pokemon_id: Union[int, None] = None
    pokeApi: Union[int, None] = None
    name: Union[str, None] = None
    created: Union[datetime, None] = None
    updated: Union[datetime, None] = None

