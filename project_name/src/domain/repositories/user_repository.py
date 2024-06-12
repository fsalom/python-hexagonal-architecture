from abc import ABC, abstractmethod

from project_name.src.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass
