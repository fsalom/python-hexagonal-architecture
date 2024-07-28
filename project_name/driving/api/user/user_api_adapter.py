from typing import List
from fastapi import APIRouter
from project_name.application.services.user_services import UserServices
from project_name.driving.api.user.models.user_dto import UserDTO
from project_name.driving.api.user.user_api_mapper import UserAPIMapper
from project_name.driven.memory.user.user_memory_adapter import InMemoryUserAdapter

router = APIRouter()
user_adapter = InMemoryUserAdapter()
service = UserServices(user_adapter)


@router.post("/users/create", response_model=UserDTO)
def create_user(user_dto: UserDTO):
    user = UserAPIMapper.from_model_to_entity(user_dto)
    service.create(user=user)


@router.get("/users/", response_model=List[UserDTO])
def list_users():
    users = service.get()
    return [UserAPIMapper.from_entity_to_model(user=user) for user in users]
