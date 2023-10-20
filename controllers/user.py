from schemas.user import UserCreate, RolCreate, RolOut
from models.user import Rol, User


def create_rol(new_rol: RolCreate, db):
    ## Acá va la logica de consulta en la base de datos

    rol = Rol(**new_rol.dict())
    db.add(rol)
    db.commit()
    db.refresh(rol)
    return rol

def exist_rol(rol_name: str, db):
    rol = db.query(Rol).filter(Rol.name == rol_name).first()
    return rol

def all_roles(db):
    return db.query(Rol).all()

def create_user(new_user: UserCreate, db):

    usr = User(**new_user.dict())
    ## Acá va la logica de consulta en la base de datos
    db.add(usr)
    db.commit()
    db.refresh(usr)
    return usr

def exist_user(email: str, db):
    usr = db.query(User).filter(User.email == email).first()
    return usr

def all_users(db):
    return db.query(User).all()

def verify_credentials(email: str, password: str, db) -> bool:
    result = db.query(User).filter(User.email == email).first()
    if result is None:
        return False
    return result.password == password






