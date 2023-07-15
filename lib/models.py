
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine( 'sqlite:///bloodoath.db' )
Session = sessionmaker( bind = engine )
session = Session()

Base = declarative_base()


class Cult( Base ):
    __tablename__ = 'cults'

    id = Column( Integer(), primary_key = True )
    name = Column( String() )
    location = Column( String() )
    founding_year = Column( Integer() )
    slogan = Column( String() )


class Follower( Base ):
    __tablename__ = 'followers'

    id = Column( Integer(), primary_key = True )
    name = Column( String() )
    age = Column( Integer() )
    life_motto = Column( String() )


class BloodOath( Base ):
    __tablename__ = 'blood_oaths'

    id = Column( Integer(), primary_key = True )
    initiation_date = Column( String() )
    cult_id = Column( Integer() )
    follower_id = Column( Integer() )
