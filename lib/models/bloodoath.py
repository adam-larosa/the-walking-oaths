from lib.walkingdev import cursor, connection






class BloodOath:
    def __init__( self, initiation_date, cult_id, follower_id, id = None ):
        self.initiation_date = initiation_date
        self.cult_id = cult_id
        self.follower_id = follower_id
        self.id = id

    
    @classmethod
    def all( cls ):
        sql = 'SELECT * FROM blood_oaths'
        rows_from_db = cursor.execute( sql ).fetchall()
        return [ cls.new_from_db( row ) for row in rows_from_db ]




    @classmethod
    def create( cls, initiation_date, cult_id, follower_id ):
        blood_oath = cls( initiation_date, cult_id, follower_id )
        blood_oath.save()
        return blood_oath
    
    def save( self ):
        sql_string = '''
            INSERT INTO blood_oaths ( 
                initiation_date, cult_id, follower_id ) VALUES ( ?, ?, ? )
        '''
        params_tuple = ( self.initiation_date, self.cult_id, self.follower_id )
        cursor.execute( sql_string, params_tuple )
        connection.commit()
        id_sql = 'SELECT last_insert_rowid() FROM blood_oaths'
        self.id = cursor.execute( id_sql ).fetchone()[0]


    
    @classmethod
    def new_from_db( cls, row ):
        oath = cls( row[1], row[2], row[3] )
        oath.id = row[0]
        return oath

    @classmethod
    def create_table( cls ):
        sql = '''
            CREATE TABLE IF NOT EXISTS blood_oaths ( 
                id INTEGER PRIMARY KEY,
                initiation_date TEXT,
                cult_id INTEGER,
                follower_id INTEGER
            )
        '''
        cursor.execute( sql )

    @classmethod
    def drop_table( cls ):
        cursor.execute( 'DROP TABLE blood_oaths' )

    @classmethod
    def erase_table( cls ):
        cursor.execute( 'DELETE FROM blood_oaths' )
        connection.commit()


    @property
    def follower( self ):
        from .follower import Follower
        sql = 'SELECT * FROM followers WHERE id = ? LIMIT 1'
        row = cursor.execute( sql, ( self.follower_id, ) ).fetchone()
        return Follower.new_from_db( row )

    @property
    def cult( self ):
        from .cult import Cult
        sql = 'SELECT * FROM cults WHERE id = ? LIMIT 1'
        row = cursor.execute( sql, ( self.cult_id, ) ).fetchone()
        return Cult.new_from_db( row )

    @classmethod
    def first_oath( cls ):
        from .follower import Follower
        sql = '''
            SELECT followers.* FROM followers
            JOIN blood_oaths ON blood_oaths.follower_id = followers.id 
            LIMIT 1
        '''
        row = cursor.execute( sql ).fetchone()
        return Follower.new_from_db( row )
        
