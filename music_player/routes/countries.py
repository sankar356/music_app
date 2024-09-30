from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from config.config import engine, Base, get_db
from models.model import Countries,StatusEnum
from schemas.countries import CountryBase
from typing import List
from sqlalchemy.exc import SQLAlchemyError

route = APIRouter()

Base.metadata.create_all(bind=engine)

@route.get("/",response_model=List[CountryBase])
def get_countries(db: Session = Depends(get_db),skip: int = 0, limit: int = 10):
    countries = db.query(Countries).offset(skip).limit(limit).all()
    return countries