from fastapi import APIRouter
from controller.pokemon import pokemon_controller
from entity.pokemon import PokemonEntity

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
async def add_one(pokemon: PokemonEntity):
    return await pokemon_controller.create_pokemon(pokemon)


@router.put("")
async def update_one(pokemon: PokemonEntity):
    return await pokemon_controller.update_pokemon(pokemon)


@router.delete("/{id}")
async def delete_one(id):
    return await pokemon_controller.delete_pokemon(id)
