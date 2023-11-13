class AbilityController:

    async def get_abilities(self):
        return ({"message": "Get all abilitys"})

    async def get_ability_by_id(self, id: int):
        return ({"message": "Get one ability by ID", "id": id})

    async def get_ability_by_name(self, name: str):
        return ({"message": "Get one ability by ID", "id": id})

    async def create_ability(self):
        return ({"message": "Create a new ability"})

    async def update_ability(self, id: int):
        return ({"message": "Update ability by ID", "id": id})

    async def delete_ability(self, id: int):
        return ({"message": "Delete ability by ID", "id": id})


ability_controller = AbilityController()
