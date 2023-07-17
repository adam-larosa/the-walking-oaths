from sqlalchemy import asc, func, distinct, Column, Integer, String
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


    
    
    
    
    
    followers = association_proxy( 'oaths', 'follower', 
        creator = lambda f : BloodOath( follower = f, initiation_date = 'now!' ) )

    
    
    
    
    
    


    def recruit_follower( self, follower, date = 'right now' ):
        from .follower import Follower
        if isinstance( follower, Follower ):
            if follower.age >= self.minimum_age:
                self.followers.append( follower )
                session.commit()
            else:
                print( 'Not yet young one, but now is not your time.' )
        else:
            return 'Argument not valid Follower instance.'


    @property
    def cult_population(self):
        query = session.query( func.count( distinct( BloodOath.follower_id ) ) )
        by_cult = query.filter( BloodOath.cult_id == self.id )
        return by_cult.scalar()  # scalar is what actually executes the SQL 
                                 # query & returns the first result, or None 






    @classmethod
    def all( cls ):
        return session.query( cls ).all()






    @classmethod
    def find_by_name( cls, search ):
        query = session.query( cls ).filter( cls.name.ilike( f'%{search}%' ) )
        return query.first()



    


    @classmethod
    def find_by_location( cls, query ):
        query = session.query( cls )
        by_location = query.filter( cls.location.ilike( f'%{search}%' ) )
        return by_location.all()


    @classmethod
    def find_by_founding_year( cls, search_year ):
        query = session.query( cls )
        return query.filter( cls.founding_year == search_year ).all()



    @property
    def average_age( self ):
        from .follower import Follower
        query = session.query( func.avg( Follower.age ) )
        return query.filter( Follower.oaths.any( cult_id = self.id ) ).scalar()






    @property
    def my_followers_mottos( self ):
        from .follower import Follower
        query = session.query( Follower.life_motto )
        by_followers = query.filter( Follower.oaths.any( cult_id = self.id ) )
        return [ query_tuple[0] for query_tuple in by_followers.all() ]






    @classmethod
    def least_popular(cls):
        query = session.query( 
            cls, 
            func.count( BloodOath.follower_id ).label( 'follower_count' ) 
        )
        with_cults = query.outerjoin( BloodOath, BloodOath.cult_id == cls.id )
        result = with_cults.group_by( cls.id )
        cult = result.order_by( asc( 'follower_count' ) ).first()
        if cult:
            return cult[0]  # order_by will return a tuple
        return None