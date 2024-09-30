from fastapi import APIRouter, Depends,HTTPException,status,Query,UploadFile,File
from sqlalchemy.orm import Session
from pydantic import ValidationError
from datetime import time , date
from config.config import engine, Base, get_db
from models.model import *
from schemas.track import TrackBase,TrackCreate 
from schemas.album import AlbumBase
from schemas.artist import ArtistBase
from config.config import UPLOAD_DIRECTORY,os
from typing import List
from sqlalchemy.exc import SQLAlchemyError



route = APIRouter()
Base.metadata.create_all(bind=engine)

@route.post("/")
async def add_track(
    title: str,artistId : int,albumId: int, duration: time,ReleaseDate:date,
    db: Session = Depends(get_db), 
    file: UploadFile = File(...)
):
    artist = db.query(Artist).filter(Artist.id == artistId).first()
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    
    album = db.query(Album).filter(Album.id == albumId).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as audio_file:
        audio_file.write(await file.read())
    
    new_track = Track(
        title=title,
        artistId=artistId, 
        albumId=albumId,  
        duration=duration,  
        ReleaseDate=ReleaseDate,  
        filePath=file_path 
    )

    
    db.add(new_track)
    db.commit()
    db.refresh(new_track)


    return new_track



@ route.get("/",response_model=List[TrackBase])
def get_album(skip : int = Query(0, ge=0), limit : int = Query(10, le=100),db : Session = Depends(get_db)):
    tracks = db.query(Track).offset(skip).limit(limit).all()
    if not tracks:
        raise HTTPException(status_code=404,detail='Track not found')
    responce = []
    
    for traack in tracks:
        track_data = TrackBase.from_orm(traack)
        track_data.filePath = traack.filePath
        if  traack.artistId:
            artist = db.query(Artist).filter(Artist.id ==traack.artistId).first()
            if artist:
                track_data.artistId = ArtistBase.from_orm(artist)
        if  traack.albumId:
            album = db.query(Album).filter(Album.id ==traack.albumId).first()
            if album:
                track_data.albumId = AlbumBase.from_orm(album)
        responce.append(track_data)
    return responce
 
    