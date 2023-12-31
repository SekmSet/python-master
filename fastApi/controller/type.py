from service.type import type_service

from entity.type import TypeEntity


class TypeController:

    async def get_types(self):
        results = await type_service.get_all()
        return {"message": "Get all types", "results": results}

    async def get_type_by_id(self, id: int):
        result = await type_service.find_by_id(id)
        return {"message": "Get one type by ID", "result": result}

    async def get_type_by_name(self, name: str):
        result = await type_service.find_by_name(name)
        return {"message": "Get one type by NAME", "result": result}

    async def create_type(self, type: TypeEntity):
        type = await type_service.create(type)
        return {"message": "✅Create a new type", "type": type}

    async def update_type(self, type: TypeEntity):
        updated = await type_service.update(type)
        return {"message": "✅Update type done", "updated type": updated}

    async def delete_type(self, id: int):
        # await type_service.delete_type(id)
        return {"message": "Delete type by ID", "id": id}


type_controller = TypeController()
