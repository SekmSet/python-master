from typing import List

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped
from db.database import Base

association_pokemon_ability = Table(
    "pokemon_ability",
    Base.metadata,
    Column("pokemon_id", ForeignKey("pokemon.id"), primary_key=True),
    Column("ability_id", ForeignKey("ability.id"), primary_key=True),
)

association_pokemon_type = Table(
    "pokemon_type",
    Base.metadata,
    Column("pokemon_id", ForeignKey("pokemon.id"), primary_key=True),
    Column("type_id", ForeignKey("type.id"), primary_key=True),
)


class Pokemon(Base):
    __tablename__ = "pokemon"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    weight = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    base_experience = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)

    # child: Mapped["Sprite"] = relationship(back_populates="pokemons")
    sprite = relationship('Sprite', back_populates='pokemon', uselist=False)
    abilities = relationship('Ability', secondary=association_pokemon_ability, back_populates='pokemons')
    types = relationship('Type', secondary=association_pokemon_type, back_populates='pokemons')

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "weight": self.weight,
            "height": self.height,
            "base_experience": self.base_experience,
            "sprite": self.sprite,
            "abilities": self.abilities,
            "types": self.types,
            "created": self.created,
            "updated": self.updated,
        }


class Ability(Base):
    __tablename__ = "ability"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    effect = Column(String(255), nullable=False)
    short_effect = Column(String(255), nullable=False)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)

    pokemons = relationship('Pokemon', secondary=association_pokemon_ability, back_populates='abilities')

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "effect": self.effect,
            "short_effect": self.short_effect,
            "created": self.created,
            "updated": self.updated,
            "pokemon_id": self.pokemon_id,
        }


class Type(Base):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)

    pokemons = relationship('Pokemon', secondary=association_pokemon_type, back_populates='types')

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "pokemon_id": self.pokemon_id,
            "created": self.created,
            "updated": self.updated,
        }


class Sprite(Base):
    __tablename__ = "sprite"

    id = Column(Integer, primary_key=True)
    front_default = Column(String(255), unique=True)
    front_shiny = Column(String(255), unique=True)
    front_shiny_female = Column(String(255), unique=True)
    back_default = Column(String(255), unique=True)
    back_female = Column(String(255), unique=True)
    back_shiny = Column(String(255), unique=True)
    back_shiny_female = Column(String(255), unique=True)
    front_female = Column(String(255), unique=True)
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)
    pokemon_id = Column(Integer, ForeignKey("pokemon.id"))

    # parent: Mapped["Pokemon"] = relationship(back_populates="sprites")
    pokemon = relationship('Pokemon', back_populates='sprite', uselist=False)

    def dict(self):
        return {
            "id": self.id,
            "front_default": self.front_default,
            "front_shiny": self.front_shiny,
            "front_shiny_female": self.front_shiny_female,
            "back_default": self.back_default,
            "back_female": self.back_female,
            "back_shiny": self.back_shiny,
            "back_shiny_female": self.back_shiny_female,
            "front_female": self.front_female,
            "created": self.created,
            "updated": self.updated,
            "pokemon_id": self.pokemon_id,
        }


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    password = Column(String(255))
    created = Column(DateTime, nullable=False)
    updated = Column(DateTime)

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "created": self.created,
            "updated": self.updated,
        }
