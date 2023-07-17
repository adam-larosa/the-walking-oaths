from .bloodoath import BloodOath









class Follower:
    all = []
    def __init__( self, name, age, life_motto ):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        Follower.all.append( self )


    
    
    @property
    def oaths( self ):
        return [ o for o in BloodOath.all if o.follower == self ]

    
    
    
    
    
    @property
    def cults( self ):
        return list( { o.cult for o in self.oaths } )




    def join_cult( self, cult, time = 'right now' ):
        from .cult import Cult
        if isinstance( cult, Cult ):
            if self.age >= cult.minimum_age:
                BloodOath( time, cult, self )
            else:
                print( 'We must wait a bit longer before we are ready' )
        else:
            return 'Argument not Cult object.'







    @classmethod
    def all( cls ):
        return cls.all





    
    @classmethod
    def of_a_certain_age( cls, query ):
        return [ f for f in cls.all if f.age >= query ]

    @property
    def my_cults_slogans( self ):
        for cult in self.cults:
            print( cult.slogan )

    @classmethod
    def most_active( cls ):
        return max( cls.all, key = lambda f : len( f.cults ) )

    @classmethod
    def top_ten( cls ):
        by_cults = lambda f : len(f.cults)
        return sorted( Follower.all, key = by_cults, reverse = True )[:10]

    @property
    def fellow_cult_members( self ):
        fellows = set()
        for cult in self.cults:
            for follower in cult.followers:
                if follower != self:
                    fellows.add( follower )
        return list( fellows )