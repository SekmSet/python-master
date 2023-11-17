from typing import Annotated
from fastapi import APIRouter, Depends
from controller.ability import ability_controller
from entity.ability import AbilityEntity
from service.middleware import get_current_user
from db.model.models import User

router = APIRouter(
    prefix='/ability',
    tags=['Ability']
)


@router.get("/list")
async def get_all():
    return await ability_controller.get_abilities()


@router.get("/id/{id}")
async def get_one(id: int):
    return await ability_controller.get_ability_by_id(id)


@router.get("/name/{name}")
async def get_one(name: str):
    return await ability_controller.get_ability_by_name(name)


@router.post("")
async def add_one(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return await ability_controller.create_ability()


@router.put("/")
async def update_one(ability: AbilityEntity, current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return await ability_controller.update_ability(ability)


@router.delete("/{id}")
async def delete_one(id: int, current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return await ability_controller.delete_ability(id)
