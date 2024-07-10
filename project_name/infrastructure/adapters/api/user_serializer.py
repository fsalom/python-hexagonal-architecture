from pydantic import BaseModel, ConfigDict, Field


class UserSerializer(BaseModel):
    name: str
    email: str
    id: int

    class Config:
        from_attributes = True
        orm_mode = True

