from pydantic import BaseModel, EmailStr,validator
from typing import Optional,Any
import re


class OtpBase(BaseModel):
    
    id: Optional[int]
    email : EmailStr
    code : int
    type : Optional[str]
    status : Optional [str]

class OtpCreate(OtpBase):
    pass