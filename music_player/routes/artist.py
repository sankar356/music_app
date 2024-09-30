from fastapi import APIRouter, Depends, HTTPException,Query
from sqlalchemy.orm import Session
from config.config import get_db, Base, engine
from models.model import Artist, StatusEnum
from schemas.artist import ArtistBase, CreateArtist
from typing import List


route = APIRouter()

Base.metadata.create_all(bind = engine) 

@route.post("/",response_model=ArtistBase)
def add_artist(artist_data :CreateArtist,db: Session = Depends(get_db)):
    artist = Artist(
        name = artist_data.name,
        genre = artist_data.genre
    )
    db.add(artist)
    db.commit()
    db.refresh(artist)
    
    return artist

@route.get("/",response_model=List[ArtistBase])
def get_artist(skip: int = Query(0, ge=0), limit: int = Query(10, le=100), db: Session = Depends(get_db)):
    artist = db.query(Artist).filter_by(status = StatusEnum.ACTIVE.value).offset(skip).limit(limit).all()
    
    return artist