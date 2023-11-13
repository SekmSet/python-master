from fastapi import APIRouter
from controller.sprite import sprite_controller

router = APIRouter(
    prefix='/sprite',
    tags=['sprite']
)


@router.get("/list")
async def get_all():
    return await sprite_controller.get_sprites()


@router.get("/id/{id}")
async def get_one_id(id: int):
    return await sprite_controller.get_sprite_by_id(id)


@router.get("/name/{name}")
async def get_one_name(name):
    return await sprite_controller.get_sprite_by_name(name)


@router.post("")
async def add_one():
    return await sprite_controller.create_sprite()


@router.put("/{id}")
async def update_one(id: int):
    return await sprite_controller.update_sprite(id)


@router.delete("/{id}")
async def delete_one(id: int):
    return await sprite_controller.delete_sprite(id)
