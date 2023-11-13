from fastapi import APIRouter
from controller.type import type_controller

router = APIRouter(
    prefix='/type',
    tags=['type']
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
async def add_one():
    return await type_controller.create_type()


@router.put("/{id}")
async def update_one(id: int):
    return await type_controller.update_type(id)


@router.delete("/{id}")
async def delete_one(id: int):
    return await type_controller.delete_type(id)
