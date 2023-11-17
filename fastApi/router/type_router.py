from typing import Annotated
from fastapi import APIRouter, Depends
from controller.type import type_controller
from entity.type import TypeEntity
from service.middleware import get_current_user
from db.model.models import User

router = APIRouter(
    prefix='/type',
    tags=['Type']
)


@router.get("/list")
async def get_all():
    return await type_controller.get_types()


@router.get("/id/{id}")
async def get_one(id: int):
    return await type_controller.get_type_by_id(id)


@router.get("/name/{name}")
async def get_one_name(name: str):
    return await type_controller.get_type_by_name(name)


@router.post("")
async def add_one(type: TypeEntity, current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return await type_controller.create_type(type)


@router.put("")
async def update_one(type: TypeEntity, current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return await type_controller.update_type(type)


@router.delete("/{id}")
async def delete_one(id: int, current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return await type_controller.delete_type(id)
