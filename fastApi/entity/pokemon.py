from pydantic import BaseModel
from typing import Union, List
from datetime import datetime

from db.model.models import Sprite, Type, Ability


class PokemonEntity(BaseModel):
    id: Union[int, None] = None
    pokeApi: Union[int, None] = None
    name: Union[str, None] = None
    weight: Union[int, None] = None
    height: Union[int, None] = None
    base_experience: Union[int, None] = None
    created: Union[datetime, None] = None
    updated: Union[datetime, None] = None
