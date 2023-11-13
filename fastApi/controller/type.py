from service.type import type_service


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

    async def create_type(self):
        return {"message": "Create a new type"}

    async def update_type(self, id: int):
        return {"message": "Update type by ID", "id": id}

    async def delete_type(self, id: int):
        return {"message": "Delete type by ID", "id": id}


type_controller = TypeController()
