from pydantic import BaseModel


class UserDB(BaseModel):
    name: str
    email: str
    id: int
