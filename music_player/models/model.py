from sqlalchemy import Column, Integer, String,DateTime,Enum,TEXT,ForeignKey,DECIMAL,Time,Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
from config.config import engine
Base = declarative_base()  
from datetime import datetime
import enum


class StatusEnum(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"

class Countries(Base):
    __tablename__ = "countries"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    shortname = Column(String(5), nullable=False)
    phonecode = Column(Integer, nullable=False)



class Roles(Base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.ACTIVE)  # Use enum value here
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
   
# class UserRole(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer,ForeignKey("users.id"))
#     role_id = Column(Integer,ForeignKey("roles.id"))
#     createdAt = Column(DateTime, default=datetime.utcnow)



class Users(Base):
    __tablename__="users"
    
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(50), unique=True, index=True)
    firstName = Column(String(50),nullable = False)
    lastName =  Column(String(50),nullable = False)
    mobileNumber = Column(String(10),nullable=False)
    country = Column(Integer,ForeignKey("countries.id"))
    email = Column(String(50),nullable=False)
    role = Column(Integer,ForeignKey("roles.id"))
    followers_count = Column(Integer, default=0)
    playlists_count = Column(Integer, default=0)
    profile_image  = Column(String(50))
    status = Column(Enum(StatusEnum),default=StatusEnum.ACTIVE.value)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
class Subscription(Base):
    __tablename__="subscription"
    
    id = Column(Integer,primary_key=True,index=True)
    name =Column(String(50),nullable=False)
    price = Column(DECIMAL(precision=10, scale=2),nullable=False)
    description = Column(TEXT,nullable=False)


class Artist(Base):
    __tablename__="artist"
    
    id = Column(Integer,primary_key = True,index = True)
    name = Column(String(50), nullable = False)
    genre = Column(String(50),nullable = False)
    status = Column(Enum(StatusEnum),default=StatusEnum.ACTIVE.value)

class Payment(Base):
    __tablename__='payment'
    
    id =Column(Integer,primary_key = True,index = True)
    userId = Column(Integer,ForeignKey('users.id'))
    amount = Column(DECIMAL(precision=10, scale=2))
    date = Column(DateTime,default=datetime.utcnow)
    method = Column(String(50))
    
class Album(Base):
    __tablename__ = 'album'
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(50),nullable=False)
    artistId = Column(Integer,ForeignKey('artist.id'))
    genre = Column(String(50),nullable = False)
    releaseDate = Column(DateTime)

class Track(Base):
    __tablename__ = 'track'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(50),nullable=False)
    artistId = Column(Integer,ForeignKey('artist.id'))
    albumId = Column(Integer,ForeignKey('album.id'))
    duration = Column(Time,nullable=False)
    ReleaseDate = Column(Date, nullable=True)
    filePath = Column(String(100), nullable=False)
    
    
class Otp(Base):
    __tablename__ = 'otps'
    id = Column(Integer,index = True,primary_key=True)
    email = Column(String(50),nullable=False)
    code = Column(Integer,nullable=False)
    type = Column(String(50),nullable=False)
    status =Column(Enum(StatusEnum))
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
Base.metadata.create_all(bind=engine)