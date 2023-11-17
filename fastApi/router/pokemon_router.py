from typing import Annotated
from typing import Annotated
from fastapi import APIRouter, Depends
from controller.pokemon import pokemon_controller
from entity.pokemon import PokemonEntity
from service.middleware import get_current_user
from db.model.models import User


router = APIRouter(
    prefix='/pokemon',
    tags=['Pokemon']
)


@router.get("/list")
async def get_all():
    return await pokemon_controller.get_pokemons()


@router.get("/id/{id}")
async def get_one_id(id: int):
    return await pokemon_controller.get_pokemon_by_id(id)


@router.get("/name/{name}")
async def get_one_name(name: str):
    return await pokemon_controller.get_pokemon_by_name(name)


@router.post("")
async def add_one(pokemon: PokemonEntity, current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return await pokemon_controller.create_pokemon(pokemon)


@router.put("")
async def update_one(pokemon: PokemonEntity, current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return await pokemon_controller.update_pokemon(pokemon)


@router.delete("/{id}")
async def delete_one(id, current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return await pokemon_controller.delete_pokemon(id)
