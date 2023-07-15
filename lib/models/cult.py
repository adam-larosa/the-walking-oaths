
from sqlalchemy import Column, Integer, String
if 'lib' in __name__ :
    from lib.walkingdev import Base, session
else:
    from walkingdev import Base, session

from .bloodoath import BloodOath


class Cult( Base ):
    __tablename__ = 'cults'

    id = Column( Integer(), primary_key = True )
    name = Column( String() )
    location = Column( String() )
    founding_year = Column( Integer() )
    slogan = Column( String() )
    meow = Column( String() )

    @classmethod
    def all( cls ):
        return session.query( cls ).all()

    # Takes in an argument of a Follower instance and adds them to this cult's 
    # list of followers.
    def recruit_follower( self, follower, date = 'right now' ):
        from .follower import Follower
        if isinstance( follower, Follower ):
            oath = BloodOath( 
                initiation_date = date, 
                follower_id = follower.id, 
                cult_id = self.id  
            )
            session.add( oath )
            session.commit()
            return oath
        else:
            return 'Argument not valid Follower instance.'
