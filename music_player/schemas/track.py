from pydantic import BaseModel, Field
from typing import Optional
from datetime import time, date

class TrackBase(BaseModel):
    id : Optional[int]
    title: str 
    artistId: int
    albumId: int
    duration: time
    ReleaseDate: Optional[date] = None
    filePath : str = Field(..., max_length=100)
    class Config:
        orm_mode = True
        from_attributes = True  
        arbitrary_types_allowed =True
class TrackCreate(TrackBase):
    pass

class TrackUpdate(TrackBase):
    title: Optional[str] = None
    artistId: Optional[int] = None
    albumId: Optional[int] = None
    duration: Optional[time] = None
    ReleaseDate: Optional[date] = None

class TrackInDB(TrackBase):
    id: int

    class Config:
        orm_mode = True
