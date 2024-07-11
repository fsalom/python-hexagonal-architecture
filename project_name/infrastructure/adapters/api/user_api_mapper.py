from pydantic import BaseModel, ConfigDict, Field

from project_name.domain.entities.user import User
from project_name.infrastructure.adapters.api.models.user_dto import UserDTO


class UserAPIMapper:

    @staticmethod
    def from_model_to_entity(self, user_dto: UserDTO) -> User:
        return User(user_id=user_dto.id, name=user_dto.name, email=user_dto.email)

    @staticmethod
    def from_entity_to_model(self, user: User) -> UserDTO:
        return UserDTO(**user)
