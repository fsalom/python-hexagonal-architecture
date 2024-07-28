from project_name.domain.entities.user import User
from project_name.application.ports.driving.user_service_port import UserPort


class UserServices(UserServicePort):
    def __init__(self, user_repository_port: UserRepositoryPort):
        self.user_repository_port = user_repository_port

    def get(self) -> [User]:
        return self.user_repository_port.list_users()

    def create(self, user: User):
        return self.user_repository_port.create(user)
