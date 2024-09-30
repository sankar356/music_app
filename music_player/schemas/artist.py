from pydantic import BaseModel, EmailStr,validator
from typing import Optional,Any
import re


class ArtistBase(BaseModel):
    id : Optional[int]
    name : str
    genre : str
    status : Optional[str]
    
    class Config:
        orm_mode = True
        from_attributes = True  
        arbitrary_types_allowed =True
    
class CreateArtist(ArtistBase):
    name : str
    genre : str