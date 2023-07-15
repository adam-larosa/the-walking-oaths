import ipdb
from lib.models import *

# test your code here
# e.g.

# f1 = Follower( 'Emiley', 31, 'Living the Dream' )
# c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )

# bo1 = BloodOath( '2019-09-16', f1, c1 )


# c1.followers => ???
# f1.cults => ???

gate = Cult( "Heaven's Gate", 'San Diego', 1974, 'Look to the stars!', 18 )
town = Cult( "People's Temple", 'San Francisco', 1954, 'Tasty Kool-Aid.', 18 )
Cult( 'Branch Davidians', 'Waco', 1955, 'Come and get it!', 18 )
wiz = Cult( 'Wizard Status', 'Seattle', 1997, 'Come and get it!', 5 )
Cult( 'Adamtown', 'San Francisco', 1997, 'COMPUTERLIFE', 18 )

adam = Follower( 'Adam', 44, 'EDM & computers plz.' )
emiley = Follower( 'Emiley', 27, 'Coffee is wonderful!' )
Follower( 'Ix', 31, '...abra Cadabra...' )

b1 = Follower( 'badcat1', 5, 'meow1' )
b2 = Follower( 'badcat2', 5, 'meow1' )
b3 = Follower( 'badcat3', 5, 'meow1' )

for f in [ b1, b2, b3 ]:
    wiz.recruit_follower( f )

for c in Cult.all:
    c.recruit_follower( emiley )

for c in [ gate, town ]:
    c.recruit_follower( adam )

print( "Mwahahaha!" )
ipdb.set_trace()