from project_name.domain.entities.user import User
from project_name.driven.db.user.models.user_db import UserDB


class UserDBMapper:
    @staticmethod
    def from_model_to_entity(user_dto: UserDB) -> User:
        return User(user_id=user_dto.id, name=user_dto.name, email=user_dto.email)

    @staticmethod
    def from_entity_to_model(user: User) -> UserDB:
        return UserDB(**user)
