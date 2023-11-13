import datetime

from entity.ability import AbilityEntity
from repository.ability import ability_repository


class AbilityService:
    async def create(self, ability: AbilityEntity):
        ability.created = datetime.datetime.now()
        created = await ability_repository.create(ability)
        return created

    async def create_pokemon_ability_link(self, pokemon_id: int, ability_id: int):
        await ability_repository.create_link(pokemon_id, ability_id)

    async def update(self, ability: AbilityEntity):
        ability.updated = datetime.datetime.now()
        return await ability_repository.update(ability)

    async def delete(self, id: int):
        await ability_repository.delete(id)

    async def get_all(self):
        return await ability_repository.get_all()

    async def find_by_id(self, id: int):
        return await ability_repository.get_one(id)

    async def find_by_name(self, name: str):
        return await ability_repository.get_by_name(name)


ability_service = AbilityService()
