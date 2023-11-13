import datetime
from repository.sprite import sprite_repository
from entity.sprite import SpriteEntity
from db.model.models import Sprite


class SpriteService:
    async def create(self, sprite: Sprite):
        sprite.created = datetime.datetime.now()
        print("sprite service")
        created = await sprite_repository.create(sprite)
        return created

    async def update(self, sprite: SpriteEntity):
        sprite.updated = datetime.datetime.now()
        return await sprite_repository.update(sprite)

    async def delete(self, id: int):
        await sprite_repository.delete(id)

    async def get_all(self):
        return await sprite_repository.get_all()

    async def find_by_id(self, id: int):
        return await sprite_repository.get_by_id(id)



sprite_service = SpriteService()
