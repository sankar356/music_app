from fastapi import APIRouter, Depends,HTTPException,status,Query
from sqlalchemy.orm import Session
from config.config import engine, Base, get_db
from models.model import Roles,StatusEnum
from models.model import Countries
from models.model import Users,StatusEnum
from schemas.users import UserBase,UserCreate
from schemas.countries import CountryBase
from schemas.role import RoleBase
from typing import List
from sqlalchemy.exc import SQLAlchemyError


route = APIRouter()

Base.metadata.create_all(bind=engine)

@route.post("/",response_model=UserBase)
def create_user(user_base : UserCreate,db: Session = Depends(get_db)):
    role = db.query(Roles).filter_by(name='User').first()
    if role:
        role_id = role.id
    else:
        role_id = None  
    country_data = db.query(Countries).filter(Countries.id == user_base.country).first()
    if not country_data:
        raise HTTPException(status_code=404, detail="country not found")
    existing_user = db.query(Users).filter(Users.username == user_base.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    existing_email = db.query(Users).filter(Users.email == user_base.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    new_user = Users(
        username=user_base.username,
        firstName=user_base.firstName,
        lastName=user_base.lastName,
        mobileNumber=user_base.mobileNumber,
        email=user_base.email,
        country=user_base.country,
        role=role_id,
        profile_image=user_base.profile_image,
        status=StatusEnum.ACTIVE.value  
    )

    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  
    
    return new_user

@route.get("/", response_model=List[UserBase])
def get_users(skip: int = Query(0, ge=0), limit: int = Query(10, le=100), db: Session = Depends(get_db)):
    users = db.query(Users).offset(skip).limit(limit).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")

    response = []
    for user in users:
        user_data = UserBase.from_orm(user)
        
        # Optionally, if you want to include full model data for role and country:
        if user.role:
            role_data = db.query(Roles).filter(Roles.id == user.role).first()
            if role_data:
                user_data.role = RoleBase.from_orm(role_data)
        
        if user.country:
            country_data = db.query(Countries).filter(Countries.id == user.country).first()
            if country_data:
                user_data.country = CountryBase.from_orm(country_data)

        response.append(user_data)
        
    return response


# @route.post("/login")




