from db.database import session
from db.model.models import Sprite
from entity.sprite import SpriteEntity


class SpriteRepo:
    async def create(self, sprite: Sprite):
        try:
            session.add(sprite)
            session.commit()
            return sprite
        except:
            return "Error during creation sprite"

    async def update(self, sprite: SpriteEntity):
        item = session.query(Sprite).get(sprite.id)

        if sprite.name and sprite.name != item.name:
            item.name = sprite.name

        if sprite.front_default and sprite.front_default != item.front_default:
            item.front_default = sprite.front_default

        if sprite.front_shiny and sprite.front_shiny != item.front_shiny:
            item.front_shiny = sprite.front_shiny

        if sprite.front_shiny_female and sprite.front_shiny_female != item.front_shiny_female:
            item.front_shiny_female = sprite.front_shiny_female

        if sprite.back_default and sprite.back_default != item.back_default:
            item.back_default = sprite.back_default

        if sprite.back_female and sprite.back_female != item.back_female:
            item.back_female = sprite.back_female

        if sprite.back_shiny and sprite.back_shiny != item.back_shiny:
            item.back_shiny = sprite.back_shiny

        if sprite.back_shiny_female and sprite.back_shiny_female != item.back_shiny_female:
            item.back_shiny_female = sprite.back_shiny_female

        item.updated = sprite.updated

        session.commit()

        return session.query(Sprite).get(sprite.id)

    async def delete(self, id: int):
        item = session.query(Sprite).get(id)
        session.delete(item)
        session.commit()

    async def get_all(self):
        return session.query(Sprite).all()

    async def get_by_id(self, id: int):
        return session.query(Sprite).get(id)


sprite_repository = SpriteRepo()
