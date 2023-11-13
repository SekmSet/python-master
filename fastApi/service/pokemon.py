import datetime
from service.request import request
from repository.pokemon import pokemon_repository
from entity.pokemon import PokemonEntity
from service.type import type_service
from db.model.models import Type
from db.model.models import Ability
from db.model.models import Sprite
from service.ability import ability_service

from service.sprite import sprite_service


async def create_type(pokemon, types):
    for type in types:
        type_name = type["type"]["name"]

        existing_type = await type_service.find_by_name(type_name)

        if not existing_type:
            convert = Type(
                name=type_name,
            )
            new_type = await type_service.create(convert)
            await type_service.create_pokemon_type_link(pokemon.id, new_type.id)
        else:
            await type_service.create_pokemon_type_link(pokemon.id, existing_type.id)


async def create_ability(pokemon, abilities):
    for ability in abilities:
        ability_name = ability["ability"]["name"]

        existing_ability = await ability_service.find_by_name(ability_name)

        if not existing_ability:
            details_ability = await request.ability_details(ability["ability"]["url"])

            for effect_entries in details_ability["effect_entries"]:
                if effect_entries["language"]["name"] == "en":
                    convert = Ability(
                        name=ability_name,
                        effect=effect_entries["effect"],
                        short_effect=effect_entries["short_effect"],
                    )
                    new_type = await ability_service.create(convert)

                    await ability_service.create_pokemon_ability_link(pokemon.id, new_type.id)
        else:
            await ability_service.create_pokemon_ability_link(pokemon.id, existing_ability.id)


class PokemonService:
    async def create(self, pokemon: PokemonEntity):
        pokemon.created = datetime.datetime.now()
        created = await pokemon_repository.create(pokemon)

        pokemon_pokeapi = await request.pokemon_details(pokemon.pokeApi)

        await create_type(created, pokemon_pokeapi['types'])
        await create_ability(created, pokemon_pokeapi['abilities'])
        await self.create_sprite(created, pokemon_pokeapi['sprites'])

        return created

    async def create_sprite(self, pokemon, sprite):
        convert = Sprite(
            back_female=sprite["back_female"],
            back_default= sprite["back_default"],
            back_shiny=sprite["back_shiny"],
            back_shiny_female=sprite["back_shiny_female"],
            front_default=sprite["front_default"],
            front_female=sprite["front_female"],
            front_shiny=sprite["front_shiny"],
            front_shiny_female=sprite["front_shiny_female"],
            pokemon_id=pokemon.id
        )
        await sprite_service.create(convert)

    async def update(self, pokemon: PokemonEntity):
        pokemon.updated = datetime.datetime.now()
        return await pokemon_repository.update(pokemon)

    async def delete(self, id: int):
        await pokemon_repository.delete(id)

    async def get_all(self):
        return await pokemon_repository.get_all()

    async def find_by_id(self, id: int):
        return await pokemon_repository.get_by_id(id)

    async def find_by_name(self, name: str):
        return await pokemon_repository.get_by_name(name)


pokemon_service = PokemonService()
