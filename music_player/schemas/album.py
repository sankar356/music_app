from pydantic import BaseModel, EmailStr,validator
from typing import Optional,Any
import re
from datetime import datetime


class AlbumBase(BaseModel):
    id : Optional [int]
    title : str
    artistId : Optional [int]
    genre : str
    releaseDate : datetime

    class Config:
        orm_mode = True
        from_attributes = True  
        arbitrary_types_allowed =True
    
class AlbumCreate(AlbumBase):
    pass