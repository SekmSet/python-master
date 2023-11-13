from db.database import session
from entity.type import TypeEntity
from db.model.models import Type
from db.model.models import Pokemon


class TypeRepo:
    async def create(self, type: TypeEntity):
        try:
            new_type = Type(
                name=type.name,
                created=type.created,
            )

            session.add(new_type)
            session.commit()

            return new_type
        except:
            return "Error during creation"

    async def create_link(self, pokemon_id: int, type_id: int):
        pokemon = session.query(Pokemon).get(pokemon_id)
        type = session.query(Type).get(type_id)

        pokemon.types.append(type)
        # type.pokemons.append(pokemon)

        session.commit()

    async def update(self, type: TypeEntity):
        item = session.query(Type).get(type.id)

        if type.name and type.name != item.name:
            item.name = type.name

        item.updated = type.updated

        session.commit()

        return session.query(Type).get(type.id)

    async def delete(self, id: int):
        item = session.query(Type).get(id)
        session.delete(item)
        session.commit()

    async def get_all(self):
        return session.query(Type).all()

    async def get_by_id(self, id: int):
        return session.query(Type).get(id)

    async def get_by_name(self, name: str):
        return session.query(Type).filter(Type.name==name).first()


type_repository = TypeRepo()
