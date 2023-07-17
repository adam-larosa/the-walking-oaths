






class BloodOath:
    all = []
    def __init__( self, initiation_date, cult_instance, follower_instance ):
        self.initiation_date = initiation_date
        self.cult = cult_instance
        self.follower = follower_instance
        BloodOath.all.append( self )


    # @property
    # def follower( self )
    #     This would be needed if we wanted a getter and setter for the 
    #     follower attribute.






    # @property
    # def cult( self )
    #     This would be needed if we wanted a getter and setter for the cult
    #     attribute.


    
    
    @classmethod
    def all( cls ):
        return cls.all



    
    @classmethod
    def first_oath( cls ):
        return cls.all[0].follower
