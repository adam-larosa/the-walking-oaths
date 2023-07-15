
from sqlalchemy import Column, Integer, String
from lib.walkingdev import Base, session

class BloodOath( Base ):
    __tablename__ = 'blood_oaths'

    id = Column( Integer(), primary_key = True )
    initiation_date = Column( String() )
    cult_id = Column( Integer() )
    follower_id = Column( Integer() )

    @classmethod
    def all( cls ):
        return session.query( cls ).all()
