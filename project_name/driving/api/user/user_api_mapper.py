from project_name.domain.entities.user import User
from project_name.driving.api.user.models.user_dto import UserDTO


class UserAPIMapper:

    @staticmethod
    def from_model_to_entity(user_dto: UserDTO) -> User:
        return User(user_id=user_dto.id, name=user_dto.name, email=user_dto.email)

    @staticmethod
    def from_entity_to_model(user: User) -> UserDTO:
        return UserDTO(id=user.user_id, name=user.name, email=user.email)
