from sqlalchemy.orm import joinedload
from db.database import session
from entity.ability import AbilityEntity
from db.model.models import Ability
from db.model.models import Pokemon


class AbilityRepo:
    async def create(self, ability: AbilityEntity):
        try:
            new_ability = Ability(
                name=ability.name,
                effect=ability.effect,
                short_effect=ability.short_effect,
                created=ability.created,
            )

            session.add(new_ability)
            session.commit()
            return new_ability
        except:
            print({"error": True, "message": "❌Error during creation ability"})

    async def create_link(self, pokemon_id: int, ability_id: int):
        pokemon = session.query(Pokemon).get(pokemon_id)
        ability = session.query(Ability).get(ability_id)

        pokemon.abilities.append(ability)
        session.commit()

    async def update(self, ability: AbilityEntity):
        try:
            item = session.query(Ability).get(ability.id)

            if ability.name and ability.name != item.name:
                item.name = ability.name
            if ability.effect and ability.effect != item.effect:
                item.effect = ability.effect
            if ability.short_effect and ability.short_effect != item.short_effect:
                item.short_effect = ability.short_effect

            item.updated = ability.updated

            session.commit()
            return session.query(Ability).get(ability.id)
        except:
            print({"error": True, "message": "❌Error during updating ability"})

    async def delete(self, id: int):
        try:
            item = session.query(Ability).get(id)
            session.delete(item)
            session.commit()
        except:
            print({"error": True, "message": "❌Error during deleting ability"})

    async def get_all(self):
        return session.query(Ability).options(joinedload(Ability.pokemons)).all()

    async def get_by_id(self, id: int):
        return session.query(Ability).options(joinedload(Ability.pokemons)).get(id)

    async def get_by_name(self, name: str):
        return session.query(Ability).options(joinedload(Ability.pokemons)).filter(Ability.name == name).first()


ability_repository = AbilityRepo()
