from fastapi import APIRouter
from controller.ability import ability_controller

router = APIRouter(
    prefix='/ability',
    tags=['ability']
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
async def add_one():
    return await ability_controller.create_ability()


@router.put("/{id}")
async def update_one(id: int):
    return await ability_controller.update_ability(id)


@router.delete("/{id}")
async def delete_one(id: int):
    return await ability_controller.delete_ability(id)
