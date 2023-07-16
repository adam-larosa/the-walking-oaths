from sqlalchemy import Column, Integer, String
if 'lib' in __name__ :                          # This if / else allows 
    from lib.walkingdev import Base, session    # the files to be used when
else:                                           # scripts use these same
    from walkingdev import Base, session        # files from different places
from sqlalchemy.orm import relationship#, backref                                                
from sqlalchemy.ext.associationproxy import association_proxy
from .bloodoath import BloodOath


class Follower( Base ):
    __tablename__ = 'followers'

    id = Column( Integer(), primary_key = True )
    name = Column( String() )
    age = Column( Integer() )
    life_motto = Column( String() )

    
    
    
    
    oaths = relationship( 'BloodOath', cascade = 'all, delete-orphan' )


    
    
    
    
    
    
    cults = association_proxy( 'oaths', 'cult', 
        creator = lambda c: BloodOath( cult = c, initiation_date = 'now!' ) )








    @classmethod
    def all( cls ):
        return session.query( cls ).all()