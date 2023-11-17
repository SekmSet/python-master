from typing import Annotated
from fastapi import APIRouter, Depends
from controller.sprite import sprite_controller
from entity.sprite import SpriteEntity
from service.middleware import get_current_user
from db.model.models import User

router = APIRouter(
    prefix='/sprite',
    tags=['Sprite']
)


@router.get("/list")
async def get_all():
    return await sprite_controller.get_sprites()


@router.get("/id/{id}")
async def get_one_id(id: int):
    return await sprite_controller.get_sprite_by_id(id)


@router.post("")
async def add_one():
    return await sprite_controller.create_sprite()


@router.put("")
async def update_one(sprite: SpriteEntity):
    return await sprite_controller.update_sprite(sprite)


@router.delete("/{id}")
async def delete_one(id: int, current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return await sprite_controller.delete_sprite(id)
