from pydantic import BaseModel
from typing import Union
from datetime import datetime

class SpriteEntity(BaseModel):
    id: Union[int, None] = None
    pokemon_id: Union[int, None] = None
    pokeApi: Union[int, None] = None
    front_default: Union[str, None] = None
    front_shiny: Union[str, None] = None
    front_shiny_female: Union[str, None] = None
    back_default: Union[str, None] = None
    back_female: Union[str, None] = None
    back_shiny: Union[str, None] = None
    back_shiny_female: Union[str, None] = None
    created: Union[datetime, None] = None
    updated: Union[datetime, None] = None
