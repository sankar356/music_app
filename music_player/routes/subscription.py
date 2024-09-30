from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from config.config import engine, Base, get_db
from models.model import Subscription
from schemas.subscription import SubscriptionBase,SubscriptionCreate
from typing import List
from sqlalchemy.exc import SQLAlchemyError

route = APIRouter()

Base.metadata.create_all(bind=engine)

@route.post("/",response_model=SubscriptionBase)
def add_Subscription(subscribe = SubscriptionCreate, db:Session = Depends(get_db)):
    sub = Subscription(
        name = subscribe.name,
        price = subscribe.price,
        description = subscribe.description
    )
    db.add(sub)
    db.commit()
    db.refresh(sub)
    
    return sub