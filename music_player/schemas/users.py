from pydantic import BaseModel, EmailStr, Field,validator
from typing import Optional
from datetime import datetime
from enum import Enum
from schemas.role import RoleBase,RoleCreate
from schemas.countries import CountryBase,CountryCreate
from models.model import StatusEnum
import re
# Assuming StatusEnum is defined somewhere in your project

# Base schema with common fields
class UserBase(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    mobileNumber: str
    email: EmailStr
    country: Optional[int] = None
    role: Optional[int] = None
    followers_count: int
    playlists_count: int
    profile_image: Optional[str] = None
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True  

    @validator('mobileNumber', always=True)
    def validate_phone_number(cls, value):
        if value and not re.match(r'^[6-9]\d{9}$', value):
            raise ValueError('Invalid phone number. Must be 10 digits starting with 6-9.')
        return value

class UserCreate(UserBase):
    pass
# Schema for updating an existing user
class UserUpdate(BaseModel):
    firstName: Optional[str] = Field(None, max_length=50)
    lastName: Optional[str] = Field(None, max_length=50)
    mobileNumber: Optional[str] = Field(None, max_length=10)
    email: Optional[EmailStr]
    country: Optional[CountryCreate]
    role: Optional[RoleCreate]
    followers_count: Optional[int]
    playlists_count: Optional[int]
    profile_image: Optional[str] = Field(None, max_length=50)
    status: Optional[StatusEnum]
    @validator('mobileNumber', always=True)
    def validate_phone_number(cls, value):
        
        if value and not re.match(r'^[6-9]\d{9}$', value):
            raise ValueError('Invalid phone number. Must be 10 digits starting with 6-9.')
        return value
# Schema for response
class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enable ORM mode for SQLAlchemy model conversion



























# from pydantic import BaseModel, EmailStr,validator
# from typing import Optional,Any
# from enum import Enum
# from schemas.countries import CountryBase
# from schemas.role import RoleBase
# import re

# class UserBase(BaseModel):
#     id : int
#     username : str
#     firstName : str
#     lastName : str
#     mobileNumber : str
#     country : CountryBase
#     email :EmailStr
#     role : RoleBase
#     followers_count : int = 0
#     playlists_count : int = 0
#     profile_image : str
#     @validator('mobileNumber', always=True)
#     def validate_phone_number(cls, value):
#         if value and not re.match(r'^[6-9]\d{9}$', value):
#             raise ValueError('Invalid phone number. Must be 10 digits starting with 6-9.')
#         return value
# class UserCreate(UserBase):
#     pass

