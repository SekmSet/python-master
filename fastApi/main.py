from fastapi import FastAPI

from db.model import models
from db.database import engine
from router import type_router, ability_router, sprite_router, pokemon_router, auth_router


app = FastAPI()
app.include_router(pokemon_router.router)
app.include_router(type_router.router)
app.include_router(ability_router.router)
app.include_router(sprite_router.router)
app.include_router(auth_router.router)

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
