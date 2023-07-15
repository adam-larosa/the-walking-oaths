from lib.walkingdev import cursor, connection
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

    @classmethod
    def all( cls ):
        sql = 'SELECT * FROM cults'
        rows_from_db = cursor.execute( sql ).fetchall()
        return [ cls.new_from_db( row ) for row in rows_from_db ]

    @property
    def save( self ):
        sql = '''
            INSERT INTO cults ( 
                name, location, founding_year, slogan, minimum_age 
            ) VALUES ( ?, ?, ?, ?, ? )
        '''
        params_tuple = ( 
            self.name, self.location, self.founding_year, self.slogan, 
            self.minimum_age 
        )
        cursor.execute( sql, params_tuple )
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


    @property
    def oaths( self ):
        sql = '''
            SELECT * FROM blood_oaths WHERE blood_oaths.cult_id = ?
        '''
        rows_from_db = cursor.execute( sql, ( self.id, ) ).fetchall()
        return [ BloodOath.new_from_db( row ) for row in rows_from_db ]
        
    @property
    def followers( self ):
        sql = '''
            SELECT DISTINCT followers.* FROM followers
            JOIN blood_oaths ON blood_oaths.follower_id = followers.id
            WHERE blood_oaths.cult_id = ?
        '''
        rows_from_db = cursor.execute( sql, ( self.id, ) ).fetchall()
        return [ Follower.new_from_db( row ) for row in rows_from_db ]


    def recruit_follower( self, follower, time = 'right now' ):
        if isinstance( follower, Follower ):
            if follower.age >= self.minimum_age:
                BloodOath.create( time, self.id, follower.id )
            else:
                print( 'Not yet young one, but now is not your time.' )
        else:
            return 'Argument not Follower object.'

    @property
    def cult_population( self ):
        sql = '''
            SELECT COUNT( DISTINCT followers.id ) FROM followers 
            JOIN blood_oaths ON blood_oaths.follower_id = followers.id 
            JOIN cults ON blood_oaths.cult_id = ?
        '''
        query_tuple = cursor.execute( sql, ( self.id, ) ).fetchone()
        return query_tuple[0]
        
    @classmethod
    def find_by_name( cls, query ):
        sql = "SELECT * FROM cults WHERE name LIKE '%' || ? || '%' LIMIT 1"
        row = cursor.execute( sql, ( query, ) ).fetchone()
        if row:
            return cls.new_from_db( row )
        return 'Cult not found'

    @classmethod
    def find_all_by_name( cls, query ):
        sql = "SELECT * FROM cults WHERE name LIKE '%' || ? || '%'"
        rows_from_db = cursor.execute( sql, ( query, ) ).fetchall()
        return [ cls.new_from_db( row ) for row in rows_from_db ]

    @classmethod
    def find_by_location( cls, query ):
        sql = "SELECT * FROM cults WHERE location LIKE '%' || ? || '%'"
        rows_from_db = cursor.execute( sql, ( query, ) ).fetchall()
        return [ cls.new_from_db( row ) for row in rows_from_db ] 

    @classmethod
    def find_by_founding_year( cls, query ):
        sql = "SELECT * FROM cults WHERE founding_year = ?"
        rows_from_db = cursor.execute( sql, ( query, ) ).fetchall()
        return [ cls.new_from_db( row ) for row in rows_from_db ]

    @property
    def average_age( self ):
        sql = '''
            SELECT AVG( followers.age ) FROM followers
            JOIN blood_oaths ON followers.id = blood_oaths.follower_id
            WHERE blood_oaths.cult_id = ?
        '''
        query_tuple = cursor.execute( sql, ( self.id, ) ).fetchone()
        return query_tuple[0]

    @property
    def my_followers_mottos( self ):
        sql = '''
            SELECT followers.life_motto FROM followers 
            JOIN blood_oaths ON blood_oaths.follower_id = followers.id 
            WHERE blood_oaths.cult_id = ?
        '''
        query_tuple = cursor.execute( sql, ( self.id, ) ).fetchall()
        for query in query_tuple:
            print( query[0] )

    @classmethod
    def least_popular( cls ):
        sql = '''
            SELECT cults.*, COUNT(followers.id) AS follower_count
            FROM cults
            JOIN blood_oaths ON cults.id = blood_oaths.cult_id
            JOIN followers ON blood_oaths.follower_id = followers.id
            GROUP BY cults.id, cults.name
            ORDER BY follower_count ASC
            LIMIT 1;
        '''
        row = cursor.execute( sql ).fetchone()
        return cls.new_from_db( row )

    @classmethod
    def most_common_location( cls ):
        sql = '''
            SELECT location, COUNT(*) AS cult_amount
            FROM cults
            GROUP BY location
            ORDER BY cult_amount DESC
            LIMIT 1;
        '''
        query_tuple = cursor.execute( sql ).fetchone()
        return query_tuple[0]
