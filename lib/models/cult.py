
from sqlalchemy import Column, Integer, String
from lib.walkingdev import Base

class Cult( Base ):
    __tablename__ = 'cults'

    id = Column( Integer(), primary_key = True )
    name = Column( String() )
    location = Column( String() )
    founding_year = Column( Integer() )
    slogan = Column( String() )

    @classmethod
    def all( cls ):
        return session.query( cls ).all()