from sqlalchemy import func, Column, Integer, String
if 'lib' in __name__ :                          # This if / else allows 
    from lib.walkingdev import Base, session    # the files to be used when
else:                                           # other scripts use these same
    from walkingdev import Base, session        # files from different places
from sqlalchemy.orm import relationship                                           
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
        creator = lambda c : BloodOath( cult = c, initiation_date = 'now!' ) )









    def join_cult( self, cult, time = 'right now' ):
        from .cult import Cult
        if isinstance( cult, Cult ):
            if self.age >= cult.minimum_age:
                self.cults.append( cult )
                session.commit()
            else:
                print( 'We must wait a bit longer before we are ready' )
        else:
            return 'Argument not Cult object.'


    @classmethod
    def all( cls ):
        return session.query( cls ).all()





    @classmethod
    def of_a_certain_age( cls, age_query ):
        return session.query( cls ).filter( cls.age >= age_query ).all()




    @property
    def my_cults_slogans( self ):
        from .cult import Cult
        query = session.query( Cult.slogan )
        by_follower = query.filter( Cult.oaths.any( follower_id = self.id ) )
        return [ result_tuple[0] for result_tuple in by_follower.all() ]






    @classmethod
    def most_active( cls ):
        subquery = session.query(
            BloodOath.follower_id, 
            func.count(BloodOath.cult_id
        ). \
            label('active_most')). \
            group_by( BloodOath.follower_id ). \
            subquery()
        
        query = session.query(cls). \
            join(subquery, cls.id == subquery.c.follower_id). \
            order_by(subquery.c.active_most.desc()). \
            limit(1)
        result = query.first()
        return result



    @classmethod
    def top_ten( cls ):
        sql = '''
            SELECT followers.*, 
            COUNT( DISTINCT blood_oaths.cult_id ) AS active_most
            FROM followers 
            JOIN blood_oaths ON followers.id = blood_oaths.follower_id
            GROUP BY followers.id, followers.name
            ORDER BY active_most DESC
            LIMIT 10;
        '''
        rows_from_db = cursor.execute( sql ).fetchall()
        return [ cls.new_from_db( row ) for row in rows_from_db ]
