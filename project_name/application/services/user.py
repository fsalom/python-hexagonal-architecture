from project_name.domain.entities.user import User
from project_name.domain.ports.user import UserPort


class UserServices:
    def __init__(self, user_port: UserPort):
        self.user_port = user_port

    def get(self) -> [User]:
        return self.user_port.list_users()

    def create(self, user: User):
        return self.user_port.create(user)
