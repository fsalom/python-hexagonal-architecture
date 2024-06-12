from project_name.src.domain.entities.user import User
from project_name.src.domain.repositories.user_repository import UserRepository


class GetUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> User:
        return self.user_repository.get(user_id)