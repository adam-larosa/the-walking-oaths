from sqlalchemy import Column, Integer, String
# Hoping to start our BloodOath program the same way for each branch, things
if 'lib' in __name__ : # got fun when files were being loaded by alembic in
    from lib.walkingdev import Base, session # the lib directory, when in root  
else: # starting debug loaded the same files from a different location.  This
    from walkingdev import Base, session # if / else was the quick fix lol! ;)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from .bloodoath import BloodOath

class Cult( Base ):
    __tablename__ = 'cults'

    id = Column( Integer(), primary_key = True )
    name = Column( String() )
    location = Column( String() )
    founding_year = Column( Integer() )
    slogan = Column( String() )
    minimum_age = Column( Integer() )

    

    
    oaths = relationship( 'BloodOath', cascade = 'all, delete-orphan' )


    
    
    
    
    
    followers = association_proxy( 'oaths', 'cult', 
        creator = lambda f : BloodOath( follower = f, initiation_date = 'now!' ) )

    
    
    
    
    
    
    def recruit_follower( self, follower, date = 'right now' ):
        from .follower import Follower
        if isinstance( follower, Follower ):
            self.followers.append( follower )
            session.commit()
        else:
            return 'Argument not valid Follower instance.'

    @classmethod
    def all( cls ):
        return session.query( cls ).all()