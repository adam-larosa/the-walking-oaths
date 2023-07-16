from lib.walkingdev import cursor, connection
from .bloodoath import BloodOath








class Follower:
    
    def __init__( self, name, age, life_motto, id = None ):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        self.id = id


    
    
    @property
    def oaths( self ):
        sql = '''
            SELECT * FROM blood_oaths WHERE blood_oaths.follower_id = ?
        '''
        rows_from_db = cursor.execute( sql, ( self.id, ) ).fetchall()
        return [ BloodOath.new_from_db( row ) for row in rows_from_db ]


    @property
    def cults( self ):
        from .cult import Cult
        sql = '''
            SELECT DISTINCT cults.* FROM cults
            JOIN blood_oaths ON blood_oaths.cult_id = cults.id
            WHERE blood_oaths.follower_id = ?
        '''
        rows_from_db = cursor.execute( sql, ( self.id, ) ).fetchall()
        return [ Cult.new_from_db( row ) for row in rows_from_db ]



    @classmethod
    def create_table( cls ):
        sql = '''
            CREATE TABLE IF NOT EXISTS followers ( 
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                life_motto TEXT
            )
        '''
        cursor.execute( sql )
    
    @classmethod
    def drop_table( cls ):
        cursor.execute( 'DROP TABLE followers' )
    
    @classmethod
    def erase_table( cls ):
        cursor.execute( 'DELETE FROM followers' )
        connection.commit()

    @classmethod
    def all( cls ):
        sql = 'SELECT * FROM followers'
        rows_from_db = cursor.execute( sql ).fetchall()
        return [ cls.new_from_db( row ) for row in rows_from_db ]

    @property
    def save( self ):
        sql = '''
            INSERT INTO followers ( name, age, life_motto ) VALUES ( ?, ?, ? )
        '''
        cursor.execute( sql, ( self.name, self.age, self.life_motto ) )
        connection.commit()
        id_sql = 'SELECT last_insert_rowid() FROM followers'
        self.id = cursor.execute( id_sql ).fetchone()[0]

    @classmethod
    def create( cls, name, age, life_motto ):
        follower = cls( name, age, life_motto )
        follower.save
        return follower

    @classmethod
    def new_from_db( cls, row ):
        follower = cls( row[1], row[2], row[3] )
        follower.id = row[0]
        return follower



    def join_cult( self, cult, time = 'right now' ):
        from .cult import Cult
        if isinstance( cult, Cult ):
            if self.age >= cult.minimum_age:
                BloodOath.create( time, cult.id, self.id )
            else:
                print( 'We must wait a bit longer before we are ready' )
        else:
            return 'Argument not Cult object.'

    @classmethod
    def of_a_certain_age( cls, query ):
        sql = 'SELECT * FROM followers WHERE age >= ?'
        rows_from_db = cursor.execute( sql, ( query, ) ).fetchall()
        return [ cls.new_from_db( row ) for row in rows_from_db ]

    @property
    def my_cults_slogans( self ):
        sql = '''
            SELECT DISTINCT cults.slogan FROM cults
            JOIN blood_oaths ON blood_oaths.cult_id = cults.id
            WHERE blood_oaths.follower_id = ?;
        '''
        query_list = cursor.execute( sql, ( self.id, ) ).fetchall()
        for query_tuple in query_list:
            print( query_tuple[0] )

    @classmethod
    def most_active( cls ):
        sql = '''
            SELECT followers.*, 
            COUNT( DISTINCT blood_oaths.cult_id ) AS active_most
            FROM followers 
            JOIN blood_oaths ON followers.id = blood_oaths.follower_id
            GROUP BY followers.id, followers.name
            ORDER BY active_most DESC
            LIMIT 1;
        '''
        row = cursor.execute( sql ).fetchone()
        return cls.new_from_db( row )
        
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

    @property
    def fellow_cult_members( self ):
        sql = '''
            SELECT DISTINCT followers.* FROM followers
            JOIN blood_oaths ON followers.id = blood_oaths.follower_id
            WHERE blood_oaths.cult_id IN (
                SELECT cult_id FROM blood_oaths WHERE follower_id = ?
            )
            AND followers.id <> ?
        '''
        rows_from_db = cursor.execute( sql, ( self.id, self.id ) ).fetchall()
        return [ Follower.new_from_db( row ) for row in rows_from_db ]
