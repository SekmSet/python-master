from entity.user import UserEntity
from service.auth import auth_service


class AuthController:

    async def sign_in(self, user: UserEntity):
        created = await auth_service.create_user(user)
        return {"message": "✅Create a new user", "user": created}

    async def log_in(self, user: UserEntity):
        token = await auth_service.log_user(user)

        if token is not None:
            return {"message": "✅User is now log", "token": token}
        else:
            return {"message": "❌User can't be log", "token": "no token to display"}


auth_controller = AuthController()
