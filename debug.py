import ipdb
from lib import *

# test your code here
# e.g.

# f1 = Follower( 'Emiley', 31, 'Living the Dream' )
# c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )

# bo1 = BloodOath( '2019-09-16', f1, c1 )


# c1.followers => ???
# f1.cults => ???

Cult( "Heaven's Gate", 'San Diego', 1974, 'Look to the stars!' )
Cult( "People's Temple", 'San Francisco', 1954, 'We serve Kool-Aid.' )
Cult( 'Branch Davidians', 'Waco', 1955, 'Come and get it!' )
Cult( 'Wizard Status', 'Seattle', 1997, 'Come and get it!' )
Cult( 'Adamtown', 'San Francisco', 1997, 'COMPUTERLIFE' )

Follower( 'Adam', 44, 'EDM & computers plz.' )
Follower( 'Emiley', 27, 'Coffee is wonderful!' )
Follower( 'Ix', 31, '...abra Cadabra...' )

adam = Follower.all[0]

town = Cult.all[-1]


print( "Mwahahaha!" )
ipdb.set_trace()