from sqlalchemy import ForeignKey, Column, Integer, String
if 'lib' in __name__ :
    from lib.walkingdev import Base, session
else:
    from walkingdev import Base, session
from sqlalchemy.orm import relationship

class BloodOath( Base ):
    __tablename__ = 'blood_oaths'

    id = Column( Integer(), primary_key = True )
    initiation_date = Column( String() )
    cult_id = Column( Integer(), ForeignKey('cults.id') )
    follower_id = Column( Integer(), ForeignKey('followers.id') )


    cult = relationship( 'Cult', back_populates = 'oaths' )
    follower = relationship('Follower', back_populates = 'oaths' )
    
    @classmethod
    def all( cls ):
        return session.query( cls ).all()
