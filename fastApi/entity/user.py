from pydantic import BaseModel


class User(BaseModel):
    id: Union[int, None] = None
    name: Union[str, None] = None
    password: Union[str, None] = None
    created: Union[datetime, None] = None
    updated: Union[datetime, None] = None
