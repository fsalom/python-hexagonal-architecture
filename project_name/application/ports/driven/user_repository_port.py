class UserRepositoryPort(ABC):
    @abstractmethod
    def create(self, user: User):
        pass

    @abstractmethod
    def list_users(self) -> [User]:
        pass