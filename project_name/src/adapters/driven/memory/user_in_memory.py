from project_name.src.domain.entities.user import User
from project_name.src.domain.repositories.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def save(self, user: User):
        self.users[user.user_id] = user

    def get(self, user_id: int) -> User:
        return self.users.get(user_id)
