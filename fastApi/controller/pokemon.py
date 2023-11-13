from entity.pokemon import PokemonEntity

from service.pokemon import pokemon_service


class PokemonController:

    async def get_pokemons(self):
        results = await pokemon_service.get_all()

        return {"message": "Get all pokemons", "pokemons": results}

    async def get_pokemon_by_id(self, id: int):
        result = await pokemon_service.find_by_id(id)
        return {"message": "Get one pokemon by ID", "result": result}

    async def get_pokemon_by_name(self, name: str):
        result = await pokemon_service.find_by_name(name)
        return ({"message": "Get one pokemon by NAME", "result": result})

    async def create_pokemon(self, pokemon: PokemonEntity):
        await pokemon_service.create(pokemon)
        return {"message": "Create a new pokemon", "pokemon": pokemon}

    async def update_pokemon(self, pokemon: PokemonEntity):
        updated = await pokemon_service.update(pokemon)

        return {"message": "Update pokemon by ID", "updated pokemon": updated}

    async def delete_pokemon(self, id: int):
        try:
            is_exist = await pokemon_service.get_one(id)
            if is_exist:
                await pokemon_service.delete(id)

            return {"message": "Success deleting pokemon"}
        except:
            return {"message": "Error during deleting"}


pokemon_controller = PokemonController()
