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

    async def delete(self, user_to_delete: UserEntity):
        session.delete(user_to_delete)
        session.commit()

    async def find_by_id(self, id: str):
        return session.query(User).get(id)

    async def find_by_name(self, name: str):
        return session.query(User).filter(User.name == name).first()


auth_repository = AuthRepo()
