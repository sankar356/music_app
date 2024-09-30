from pydantic import BaseModel
from typing import Optional,Any
from datetime import datetime
import re

class RoleBase(BaseModel):
    id : Optional[int]
    name : str
    status : Optional[str]
    # created_at : Optional[datetime]
    # updated_at : Optional[datetime]
    class Config:
        orm_mode = True 
        from_attributes = True 
class RoleCreate(RoleBase):
    name : str
    
class RoleResponce(BaseModel):
    id:int
    name:str
    

    