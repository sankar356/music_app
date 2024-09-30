from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from config.config import engine, Base, get_db
from models.model import Roles,StatusEnum
from schemas.role import RoleBase,RoleCreate,RoleResponce
from typing import List
from sqlalchemy.exc import SQLAlchemyError


route = APIRouter()

Base.metadata.create_all(bind=engine)


@route.post("/",response_model= RoleBase)
def add_role(role:RoleCreate,db:Session = Depends(get_db)):
    db_role = Roles(
        name = role.name
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

@route.get("/",response_model=List[RoleBase])
def get_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    roles = db.query(Roles).filter_by(status=StatusEnum.ACTIVE).offset(skip).limit(limit).all()
    return roles