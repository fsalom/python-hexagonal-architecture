from project_name.domain.entities.user import User
from project_name.domain.ports.user import UserPort


class InMemoryUserAdapter(UserPort):
    def __init__(self):
        self.users = [
            User(user_id=1, name="John Doe", email="john.doe@example.com"),
            User(user_id=2, name="Jane Smith", email="jane.smith@example.com"),
            User(user_id=3, name="Alice Johnson", email="alice.johnson@example.com"),
        ]

    def create(self, user: User):
        self.users[user.user_id] = user

    def list_users(self) -> [User]:
        return self.users
