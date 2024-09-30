from pydantic import BaseModel
from typing import Optional,Any
from datetime import datetime
from decimal import Decimal
import re

class SubscriptionBase(BaseModel):
    id :Optional [int]
    name : str
    price : Decimal
    description : str
    
class SubscriptionCreate(SubscriptionBase):

    name : str
    price : Decimal
    description : str
    