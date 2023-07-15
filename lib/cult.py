from config import cursor, connection
from .bloodoath import BloodOath
from .follower import Follower

class Cult:

    def __init__( self, name, location, founding_year, slogan, minimum_age, 
                  id = None ):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        self.minimum_age = minimum_age
        self.id = id

    @classmethod
    def create_table( cls ):
        sql = '''
            CREATE TABLE IF NOT EXISTS cults ( 
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT,
                founding_year INTEGER,
                slogan TEXT,
                minimum_age INTEGER
            )
        '''
        cursor.execute( sql )

    @classmethod
    def drop_table( cls ):
        cursor.execute( 'DROP TABLE cults' )

    @classmethod
    def erase_table( cls ):
        cursor.execute( 'DELETE FROM cults' )
        connection.commit()

    @property
    def save( self ):
        sql = '''
            INSERT INTO cults ( 
                name, location, founding_year, slogan, minimum_age 
            ) VALUES ( ?, ?, ?, ?, ? )
        '''
        params = ( 
            self.name, self.location, self.founding_year, self.slogan, 
            self.minimum_age 
        )
        cursor.execute( sql, params )
        connection.commit()
        id_sql = 'SELECT last_insert_rowid() FROM cults'
        self.id = cursor.execute( id_sql ).fetchone()[0]

    @classmethod
    def create( cls, name, location, founding_year, slogan, minimum_age ):
        cult = cls( name, location, founding_year, slogan, minimum_age )
        cult.save
        return cult

    @classmethod
    def new_from_db( cls, row ):
        cult = cls( row[1], row[2], row[3], row[4], row[5] )
        cult.id = row[0]
        return cult

# ---------------------bookmark, below is unported -------------------------

    @property
    def oaths( self ):
        return [ bo for bo in BloodOath.all if bo.cult == self ]

    @property
    def followers( self ):
        return list( { bo.follower for bo in self.oaths } )


    def recruit_follower( self, follower, time = 'right now' ):
        if isinstance( follower, Follower ):
            if follower.age >= self.minimum_age:
                BloodOath( time, self, follower )
            else:
                print( 'Not yet young one, but now is not your time.' )
        else:
            return 'Argument not Follower object.'

    @property
    def cult_population( self ):
        return len( self.followers )

    @classmethod
    def find_by_name( cls, query ):
        for cult in cls.all:
            if query.lower() in cult.name.lower():
                return cult
        return 'Cult not found'

    @classmethod
    def find_all_by_name( cls, query ):
        return [ c for c in cls.all if query.lower() in c.name.lower() ]    

    @classmethod
    def find_by_location( cls, query ):
        return [ c for c in cls.all if query.lower() in c.location.lower() ]

    @classmethod
    def find_by_founding_year( cls, query ):
        return [ c for c in cls.all if query == c.founding_year ]

    @property
    def average_age( self ):
        ages = sum( [ f.age for f in self.followers ] )
        followers = len( self.followers )
        return ages / followers

    @property
    def my_followers_mottos( self ):
        for f in self.followers:
            print( f.life_motto )

    @classmethod
    def least_popular( cls ):
        by_population = lambda c : c.cult_population
        return sorted( cls.all, key = by_population )[0]

    @classmethod
    def most_common_location( self ):
        count = {}
        for cult in Cult.all:
            if count.get( cult.location ):
                count[ cult.location ] += 1
            else:
                count[ cult.location ] = 1
        return max( count, key = count.get )




              