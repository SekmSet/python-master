from db.database import session
from db.model.models import User
from entity.user import UserEntity


class AuthRepo:
    async def create(self, user: UserEntity):
        try:
            new_user = User(
                name=user.name,
                password=user.password,
                created=user.created,
            )

            session.add(new_user)
            session.commit()
            return new_user
        except:
            print({"error": True, "message": "❌Error during creating new user"})

    async def get_user_by_name(self, name):
        return session.query(User).filter(User.name == name).first()


auth_repository = AuthRepo()
