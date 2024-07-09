from typing import List
from fastapi import APIRouter
from project_name.application.services.user import UserServices
from project_name.infrastructure.adapters.user.user_in_memory import InMemoryUserAdapter
from project_name.infrastructure.api.serializers.user.user_serializer import UserSerializer

router = APIRouter()
user_adapter = InMemoryUserAdapter()
service = UserServices(user_adapter)


@router.post("/users/", response_model=UserSerializer)
def create_user(user_data: UserSerializer):
    service.create(user=user_data)


@router.get("/users/", response_model=List[UserSerializer])
def list_users():
    users = service.get()
    return [UserSerializer.from_orm(user) for user in users]
