from typing import Annotated

from fastapi import APIRouter, Depends
from entity.user import UserEntity
from controller.auth import auth_controller
from db.model.models import User
from service.middleware import get_current_user

router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)

@router.post("/signin")
async def signin(user: UserEntity):
    return await auth_controller.sign_in(user)


@router.post("/login")
async def login(user: UserEntity):
    return await auth_controller.log_in(user)


@router.get("/me")
async def read_users_me(
        current_user: Annotated[User, Depends(get_current_user)]
):

    return current_user


@router.post("/logout")
async def logout():
    pass


@router.post("/delete")
async def delete():
    pass
