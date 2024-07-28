from abc import ABC, abstractmethod

from project_name.domain.entities.user import User


class UserServicePort(ABC):
    @abstractmethod
    def create(self, user: User):
        pass

    @abstractmethod
    def list_users(self) -> [User]:
        pass
