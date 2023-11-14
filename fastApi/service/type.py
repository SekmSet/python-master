import datetime

from entity.type import TypeEntity
from repository.type import type_repository


class TypeService:
    async def create(self, type: TypeEntity):
        type.created = datetime.datetime.now()
        created = await type_repository.create(type)
        return created

    async def create_pokemon_type_link(self, pokemon_id: int, type_id: int):
        await type_repository.create_link(pokemon_id, type_id)

    async def update(self, type: TypeEntity):
        is_exist = await type_repository.get_by_id(type.id)

        if is_exist:
            type.updated = datetime.datetime.now()
            return await type_repository.update(type)

    async def delete(self, id: int):
        is_exist = type_repository.get_by_id(id)

        if is_exist:
            await type_repository.delete(id)

    async def get_all(self):
        return await type_repository.get_all()

    async def find_by_id(self, id: int):
        return await type_repository.get_by_id(id)

    async def find_by_name(self, name: str):
        return await type_repository.get_by_name(name)


type_service = TypeService()
