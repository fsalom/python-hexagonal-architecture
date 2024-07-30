from project_name.application.ports.driven.user_repository_port import UserRepositoryPort
from project_name.domain.entities.user import User
from project_name.driven.memory.user.models.user_dto import UserDTO
from project_name.driven.memory.user.user_memory_mapper import UserInMemoryMapper


class InMemoryUserAdapter(UserRepositoryPort):
    def __init__(self):
        self.users = [
            UserDTO(id=1, name="John Doe", email="john.doe@example.com"),
            UserDTO(id=2, name="Jane Smith", email="jane.smith@example.com"),
            UserDTO(id=3, name="Alice Johnson", email="alice.johnson@example.com"),
        ]

    def create(self, user: User):
        self.users[user.id] = user

    def list_users(self) -> [User]:
        return [UserInMemoryMapper.from_model_to_entity(user_dto=user) for user in self.users]
