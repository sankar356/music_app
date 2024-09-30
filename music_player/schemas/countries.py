from pydantic import BaseModel, EmailStr,validator
from typing import Optional,Any
import re


class CountryBase(BaseModel):
    id : int
    name: str
    shortname: str
    phonecode: int
    class Config:
        orm_mode = True 
        from_attributes = True 
class CountryCreate(CountryBase):
    pass

class CountryUpdate(BaseModel):
    name: Optional[str] = None
    shortname: Optional[str] = None
    phonecode: Optional[int] = None

class CountryInDB(CountryBase):
    id: int