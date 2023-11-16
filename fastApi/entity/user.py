from datetime import datetime
from typing import Union
from pydantic import BaseModel


class UserEntity(BaseModel):
    id: Union[int, None] = None
    name: Union[str, None] = None
    password: Union[str, None] = None
    created: Union[datetime, None] = None
    updated: Union[datetime, None] = None
