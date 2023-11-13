from service.ability import ability_service


class AbilityController:

    async def get_abilities(self):
        results = await ability_service.get_all()
        return {"message": "Get all abilities", "results": results}

    async def get_ability_by_id(self, id: int):
        result = await ability_service.find_by_id(id)
        return {"message": "Get one ability by ID", "result": result}

    async def get_ability_by_name(self, name: str):
        result = await ability_service.find_by_name(name)
        return {"message": "Get one ability by NAME", "result": result}

    async def create_ability(self):
        return {"message": "Create a new ability"}

    async def update_ability(self, id: int):
        return {"message": "Update ability by ID", "id": id}

    async def delete_ability(self, id: int):
        return {"message": "Delete ability by ID", "id": id}


ability_controller = AbilityController()
