from service.sprite import sprite_service
from entity.sprite import SpriteEntity

from db.model.models import Sprite


class SpriteController:

    async def get_sprites(self):
        results = await sprite_service.get_all()
        return {"message": "Get all sprites", "results": results}

    async def get_sprite_by_id(self, id: int):
        result = await sprite_service.find_by_id(id)
        return {"message": "Get one sprite by ID", "result": result}

    async def create_sprite(self, sprite: Sprite):
        created = await sprite_service.create(sprite)
        return {"message": "✅Create a new sprite", "created": created}

    async def update_sprite(self, sprite: SpriteEntity):
        return {"message": "Update sprite by ID", "id": id}

    async def delete_sprite(self, id: int):
        await sprite_service.delete(id)
        return {"message": "❌Delete sprite was correctly deleted"}


sprite_controller = SpriteController()
