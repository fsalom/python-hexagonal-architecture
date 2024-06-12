from project_name.src.domain.entities.user import User
from project_name.src.domain.repositories.user_repository import UserRepository


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int, name: str, email: str):
        user = User(user_id, name, email)
        self.user_repository.save(user)