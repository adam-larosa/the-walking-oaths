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
        return [ o.cult for o in self.oaths ]

    def join_cult( self, cult, time = 'right now' ):
        from .cult import Cult
        if isinstance( cult, Cult ):
            BloodOath( time, cult, self )
        else:
            return 'Argument not Cult object.'
    
    @classmethod
    def of_a_certain_age( cls, query ):
        follower_list = []        
        for follower in cls.all:
            if follower.age >= query:
                follower_list.append( follower )
        return follower_list

