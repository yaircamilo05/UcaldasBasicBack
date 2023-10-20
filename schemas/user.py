from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    rol_id: int

class UserCreate(User):
    password: str

class RolCreate(BaseModel):
    name: str

class RolOut(RolCreate):
    id: int 

class Userlogin(BaseModel):
    email: str
    password: str

