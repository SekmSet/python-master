class TypeController:

    async def get_types(self):
        return ({"message": "Get all types"})

    async def get_type_by_id(self, id: int):
        return ({"message": "Get one type by ID", "id": id})

    async def get_type_by_name(self, name: str):
        return ({"message": "Get one type by ID", "name": name})

    async def create_type(self):
        return ({"message": "Create a new type"})

    async def update_type(self, id: int):
        return ({"message": "Update type by ID", "id": id})

    async def delete_type(self, id: int):
        return ({"message": "Delete type by ID", "id": id})


type_controller = TypeController()
