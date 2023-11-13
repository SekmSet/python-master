from sqlalchemy.orm import joinedload
from db.model.models import Pokemon
from entity.pokemon import PokemonEntity
from db.database import session


class PokemonRepo:
    async def create(self, pokemon: PokemonEntity):
        try:
            new_pokemon = Pokemon(
                name=pokemon.name,
                weight=pokemon.weight,
                height=pokemon.height,
                base_experience=pokemon.base_experience,
                created=pokemon.created,
            )

            session.add(new_pokemon)
            session.commit()
            return new_pokemon
        except:
            return "Error during creation pokemon"

    async def update(self, pokemon: PokemonEntity):
        item = session.query(Pokemon).get(pokemon.id)

        if pokemon.name and pokemon.name != item.name:
            item.name = pokemon.name
        if pokemon.weight and pokemon.weight != item.weight:
            item.weight = pokemon.weight
        if pokemon.height and pokemon.height != item.height:
            item.height = pokemon.height
        if pokemon.base_experience and pokemon.base_experience != item.base_experience:
            item.base_experience = pokemon.base_experience

        item.updated = pokemon.updated

        session.commit()
        return session.query(Pokemon).get(pokemon.id)

    async def delete(self, id: int):
        item = session.query(Pokemon).get(id)
        session.delete(item)
        session.commit()

    async def get_all(self):
        return session.query(Pokemon).options(joinedload(Pokemon.sprite), joinedload(Pokemon.abilities), joinedload(Pokemon.types)).all()

    async def get_by_id(self, id: int):
        return session.query(Pokemon).options(joinedload(Pokemon.sprite), joinedload(Pokemon.abilities), joinedload(Pokemon.types)).get(id)


    async def get_by_name(self, name: str):
        return session.query(Pokemon).options(joinedload(Pokemon.sprite), joinedload(Pokemon.abilities), joinedload(Pokemon.types)).filter(Pokemon.name==name).first()


pokemon_repository = PokemonRepo()
