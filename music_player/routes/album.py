from fastapi import APIRouter, Depends,HTTPException,status,Query
from sqlalchemy.orm import Session
from config.config import engine, Base, get_db
from models.model import Album,Artist,StatusEnum
from schemas.album import AlbumBase,AlbumCreate
from schemas.artist import ArtistBase
from typing import List

route = APIRouter()

Base.metadata.create_all(bind=engine)

@route.post('/',response_model=AlbumBase)
def create_album(album_base : AlbumCreate,db : Session =Depends(get_db)):
    artist = db.query(Artist).filter(Artist.id ==album_base.artistId).first()
    if not artist:
        raise HTTPException(status_code=404, detail="artist not found")
    
    album = Album(
        title = album_base.title,
        artistId = album_base.artistId,
        genre = album_base.genre,
        releaseDate = album_base.releaseDate
    )
    db.add(album)
    db.commit()
    db.refresh(album)
    
    return album

@route.get('/',response_model=List[AlbumBase])
def get_album(skip : int = Query(0, ge=0), limit : int = Query(10, le=100),db : Session = Depends(get_db)):
    albums = db.query(Album).offset(skip).limit(limit).all()
    if not albums:
        raise HTTPException(status_code=404,detail='album not found')
    responce = []
    
    for album in albums:
        album_data = AlbumBase.from_orm(album)
        if  album.artistId:
            artist = db.query(Artist).filter(Artist.id ==album.artistId).first()
            if artist:
                album_data.artistId = ArtistBase.from_orm(artist)
        responce.append(album_data)
    return responce
