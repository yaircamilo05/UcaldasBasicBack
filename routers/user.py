from fastapi import APIRouter, Depends
from schemas.user import User, UserCreate, RolCreate, Userlogin
from database.db import get_db
from sqlalchemy.orm import Session
from controllers.user import create_user, create_rol, exist_rol, all_roles, exist_user, all_users, verify_credentials

from utils.auth import generate_token

router = APIRouter()

@router.post("/role")
def create_new_role(new_rol: RolCreate, db: Session = Depends(get_db)):
    exist = exist_rol(new_rol.name, db)
    if exist:
        return {"message": "Rol already exist"}

    rol = create_rol(new_rol, db)
    return rol

@router.get("/role",response_model=list[RolCreate])
def get_all_roles(db: Session = Depends(get_db)):
    return all_roles(db)

## Usuarios

#nuevo usuario
@router.post("/")
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    exist = exist_user(user.email, db)
    if exist:
        return {"message": "User already exist"}
    new_user = create_user(user,db)
    return User(**new_user.__dict__)


#obtener usuario por id
@router.get("/{mail}")
def get_user(mail: str, db: Session = Depends(get_db)):
    exist = exist_user(mail, db)
    if not exist:
        return {"message": "User not exist"}
    
    return User(**exist.__dict__)
    

#obtener todos los usuarios
@router.get("/all/", response_model=list[User])
def get_all_users(db: Session = Depends(get_db)):
    return all_users(db)

# login
@router.post("/login")
def autentication(cred:Userlogin, db: Session = Depends(get_db)):
    result = verify_credentials(cred.email, cred.password, db)

    if not result:
        return {"message": "User not authenticated"}
    
    token = generate_token()
    return token



