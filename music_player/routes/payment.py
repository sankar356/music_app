from fastapi import APIRouter, Depends,HTTPException,status,Query
from sqlalchemy.orm import Session
from config.config import engine, Base, get_db
from models.model import Users,Payment,StatusEnum
from schemas.users import UserBase
from schemas.payment import PaymentBase,PaymentCreate
from typing import List
from sqlalchemy.exc import SQLAlchemyError


route = APIRouter()

Base.metadata.create_all(bind=engine)

@route.post('/',response_model= PaymentBase)
def create_payment(payment_base: PaymentCreate, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.id == payment_base.userId).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    payment = Payment(
        userId=payment_base.userId,
        amount=payment_base.amount,
        method=payment_base.method
    )
    
    db.add(payment)
    db.commit()
    db.refresh(payment)    
    return payment


@route.get('/',response_model=List[PaymentBase])
def get_payment(skip : int = Query(0, ge=0), limit : int = Query(10, le=100),db : Session = Depends(get_db)):
    payments = db.query(Payment).offset(skip).limit(limit).all()
    if not payments:
        raise HTTPException(status_code=404,detail='no payment found')
    
    response = []
    for payment in payments:
        payment_data = PaymentBase.from_orm(payment)
        
        if payment.userId:
            user_data = db.query(Users).filter(Users.id == payment.userId).first()
            if user_data:
                payment_data.userId = UserBase.from_orm(user_data)
        
        response.append(payment_data)
    return response