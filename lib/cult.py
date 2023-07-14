from .bloodoath import BloodOath
from .follower import Follower

class Cult:
    all = []
    def __init__( self, name, location, founding_year, slogan ):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        Cult.all.append( self )

    def recruit_follower( self, follower, time = 'right now' ):
        if isinstance( follower, Follower ):
            BloodOath( time, self, follower )
        else:
            return 'Argument not Follower object.'
    
    @property
    def oaths( self ):
        return [ bo for bo in BloodOath.all if bo.cult == self ]

    @property
    def folllowers( self ):
        return list( { bo.follower for bo in self.oaths } )

    def cult_population( self ):
        return len( self.followers )

    @classmethod
    def find_by_name( cls, query ):
        for cult in cls.all:
            if query.lower() in cult.name.lower():
                return cult
        return 'Cult not found'

    @classmethod
    def find_by_location( cls, query ):
        cult_list = []
        for cult in cls.all:
            import ipdb; ipdb.set_trace()
            if query.lower() in cult.location.lower():
                cult_list.append( cult )
        return cult_list

    @classmethod
    def find_by_founding_year( cls, query ):
        cult_list = []
        for cult in cls.all:
            if query == cult.founding_year:
                cult_list.append( cult )
        return cult_list

