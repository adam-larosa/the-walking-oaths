from sqlalchemy import Column, Integer, String
if 'lib' in __name__ :
    from lib.walkingdev import Base, session
else:
    from walkingdev import Base, session


class Follower( Base ):
    __tablename__ = 'followers'

    id = Column( Integer(), primary_key = True )
    name = Column( String() )
    age = Column( Integer() )
    life_motto = Column( String() )

    @classmethod
    def all( cls ):
        return session.query( cls ).all()