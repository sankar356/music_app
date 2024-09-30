from pydantic import BaseModel, EmailStr,validator
from typing import Optional,Any
from decimal import Decimal
import re
from datetime import datetime


class PaymentBase(BaseModel):
    id : Optional [int]
    userId : Optional [int]
    amount : Decimal
    method : str
    
    class Config:
        orm_mode = True
        from_attributes = True  
        arbitrary_types_allowed =True

class PaymentCreate(PaymentBase):
    pass


