import datetime
from typing import Union
from jose import JWTError, jwt
from passlib.context import CryptContext
from repository.auth import auth_repository
from entity.user import UserEntity
from jwt.conf import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:

    async def create_user(self, user: UserEntity):
        try:
            user.created = datetime.datetime.now()
            if user.password:
                user.password = self.get_password_hash(user.password)
            return await auth_repository.create(user)
        except Exception as err:
            print({"failed": True, "message": "❌User has no password", "error": err})

    async def log_user(self, user: UserEntity):
        is_auth = await self.authenticate_user(user)

        if is_auth is not False:
            access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

            access_token = self.create_access_token(
                data={"sub": user.name},
                expires_delta=access_token_expires
            )
            return {"access_token": access_token, "token_type": "bearer"}

    def create_access_token(self, data: dict, expires_delta: Union[datetime.timedelta, None] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.datetime.now() + expires_delta
        else:
            expire = datetime.datetime.now() + datetime.timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    async def authenticate_user(self, user: UserEntity):
        is_exist = await auth_repository.get_user_by_name(user.name)

        if not is_exist:
            return False
        if not self.verify_password(user.password, is_exist.password):
            return False
        return user

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        return pwd_context.hash(password)


auth_service = AuthService()
