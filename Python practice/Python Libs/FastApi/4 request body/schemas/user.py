from pydantic import BaseModel
from utils.roles import Role
class User(BaseModel):
    username: str 
    email: str 
    password: str 
    role: Role = Role.USER