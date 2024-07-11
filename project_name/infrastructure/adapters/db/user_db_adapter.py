from project_name.domain.entities.user import User
from project_name.domain.ports.user import UserPort
from project_name.infrastructure.adapters.db.models.user_dto import UserDTO
from project_name.infrastructure.adapters.db.user_db_mapper import UserDBMapper


class InMemoryUserAdapter(UserPort):
    def __init__(self):
        self.users = [
            UserDTO(user_id=1, name="John Doe", email="john.doe@example.com"),
            UserDTO(user_id=2, name="Jane Smith", email="jane.smith@example.com"),
            UserDTO(user_id=3, name="Alice Johnson", email="alice.johnson@example.com"),
        ]

    def create(self, user: User):
        self.users[user.user_id] = user

    def list_users(self) -> [User]:
        users = [UserDBMapper.from_entity_to_model(user) for user in users]
        return users
