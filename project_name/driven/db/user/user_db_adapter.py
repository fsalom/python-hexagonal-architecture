from project_name.application.ports.driven.user_repository_port import UserRepositoryPort
from project_name.domain.entities.user import User
from project_name.driven.db.user.models.user_db import UserDB
from project_name.driven.db.user.user_db_mapper import UserDBMapper


class DBUserAdapter(UserRepositoryPort):
    def __init__(self):
        self.users = [
            UserDB(id=1, name="John Doe", email="john.doe@example.com"),
            UserDB(id=2, name="Jane Smith", email="jane.smith@example.com"),
            UserDB(id=3, name="Alice Johnson", email="alice.johnson@example.com"),
        ]

    def create(self, user: User):
        self.users[user.id] = user

    def list_users(self) -> [User]:
        return [UserDBMapper.from_model_to_entity(user_dto=user) for user in self.users]
