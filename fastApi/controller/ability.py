from service.ability import ability_service
from entity.ability import AbilityEntity


class AbilityController:

    async def get_abilities(self):
        results = await ability_service.get_all()
        return {"message": "Get all abilities", "Results": results}

    async def get_ability_by_id(self, id: int):
        result = await ability_service.find_by_id(id)
        return {"Message": "Get one ability by ID", "Result": result}

    async def get_ability_by_name(self, name: str):
        result = await ability_service.find_by_name(name)
        return {"Message": "Get one ability by NAME", "Result": result}

    async def create_ability(self):
        return {"Message": "Create a new ability"}

    async def update_ability(self, ability: AbilityEntity):
        updated = await ability_service.update(ability)
        return {"Message": "✅Update ability succeed", "Updated": updated}

    async def delete_ability(self, id: int):
        return {"Message": "❌Delete ability by ID", "id": id}


ability_controller = AbilityController()
