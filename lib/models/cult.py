from .bloodoath import BloodOath









class Cult:
    all = []
    def __init__( self, name, location, founding_year, slogan, minimum_age ):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        self.minimum_age = minimum_age
        Cult.all.append( self )



    @property
    def oaths( self ):
        return [ bo for bo in BloodOath.all if bo.cult == self ]





    @property
    def followers( self ):
        return list( { bo.follower for bo in self.oaths } )


    




    
    
    def recruit_follower( self, follower, time = 'right now' ):
        from .follower import Follower
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
    def all( cls ):
        return cls.all






    @classmethod
    def find_by_name( cls, query ):
        for cult in cls.all:
            if query.lower() in cult.name.lower():
                return cult
        return 'Cult not found'

   
   

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




              