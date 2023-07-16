






class BloodOath:
    all = []
    def __init__( self, initiation_date, cult, follower ):
        self.initiation_date = initiation_date
        self.cult = cult
        self.follower = follower
        BloodOath.all.append( self )


    






    @classmethod
    def first_oath( cls ):
        return cls.all[0].follower








    @classmethod
    def all( cls ):
        return cls.all




