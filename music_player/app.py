from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from routes.role import route as RolesRoute
from routes.countries import route as CountRoute
from routes.users import route as UserRoute
from routes.album import route as AlbumRoute
from routes.artist import route as ArtistRoute
from routes.track import route as TrackRoute
from routes.subscription import route as SubRoute
from routes.payment import route as PayRoute


app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to music world."}

app.include_router(UserRoute,tags=["users"],prefix="/api/v1/users")
app.include_router(TrackRoute,tags=["track"],prefix="/track")
app.include_router(AlbumRoute,tags=["album"],prefix="/album")
app.include_router(PayRoute,tags=["payment"],prefix="/payment")
app.include_router(ArtistRoute,tags=["artist"],prefix="/artist")
app.include_router(SubRoute,tags=["subscription"],prefix="/subscription")
app.include_router(RolesRoute,tags=["roles"],prefix="/roles")
app.include_router(CountRoute,tags=["countries"],prefix="/countries")
