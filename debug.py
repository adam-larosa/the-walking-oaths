import ipdb
from lib import *

# test your code here
# e.g.

# f1 = Follower( 'Emiley', 31, 'Living the Dream' )
# c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )

# bo1 = BloodOath( '2019-09-16', f1, c1 )


# c1.followers => ???
# f1.cults => ???

# gate = Cult( "Heaven's Gate", 'San Diego', 1974, 'Look to the stars!', 18 )
# town = Cult( "People's Temple", 'San Francisco', 1954, 'Tasty Kool-Aid.', 18 )
# Cult( 'Branch Davidians', 'Waco', 1955, 'Come and get it!', 18 )
# wiz = Cult( 'Wizard Status', 'Seattle', 1997, 'Come and get it!', 5 )
# Cult( 'Adamtown', 'San Francisco', 1997, 'COMPUTERLIFE', 18 )

# adam = Follower( 'Adam', 44, 'EDM & computers plz.' )
# emiley = Follower( 'Emiley', 27, 'Coffee is wonderful!' )
# Follower( 'Ix', 31, '...abra Cadabra...' )

# b1 = Follower( 'badcat1', 5, 'meow1' )
# b2 = Follower( 'badcat2', 5, 'meow1' )
# b3 = Follower( 'badcat3', 5, 'meow1' )

# for f in [ b1, b2, b3 ]:
#     wiz.recruit_follower( f )

# for c in Cult.all:
#     c.recruit_follower( emiley )

# for c in [ gate, town ]:
#     c.recruit_follower( adam )


# -------------------------begin porting ----------------------------
Cult.create_table()
Follower.create_table()
BloodOath.create_table()

for model in [ Cult, Follower, BloodOath ]:
    model.erase_table()


gate = Cult.create( "Heaven's Gate", 'San Diego', 1974, 'Look to the stars!', 18 )
town = Cult.create( "People's Temple", 'San Francisco', 1954, 'Tasty Kool-Aid.', 18 )
branch = Cult.create( 'Branch Davidians', 'Waco', 1955, 'Come and get it!', 18 )
wiz = Cult.create( 'Wizard Status', 'Seattle', 1997, 'Come and get it!', 5 )
Cult.create( 'Adamtown', 'San Francisco', 1997, 'COMPUTERLIFE', 18 )

adam = Follower.create( 'Adam', 44, 'EDM & computers plz.' )
emiley = Follower.create( 'Emiley', 27, 'Coffee is wonderful!' )
ix = Follower.create( 'Ix', 31, '...abra Cadabra...' )

b1 = Follower.create( 'badcat1', 5, 'meow1' )
b2 = Follower.create( 'badcat2', 5, 'meow1' )
b3 = Follower.create( 'badcat3', 5, 'meow1' )


bo1 = BloodOath.create( 'right now', gate.id, adam.id )
bo2 = BloodOath.create( 'yesterday', town.id, adam.id )
BloodOath.create( 'right now again', gate.id, adam.id )


BloodOath.create( 'emiley takes the lead', gate.id, emiley.id )
BloodOath.create( 'emiley takes the lead', town.id, emiley.id )
BloodOath.create( 'emiley takes the lead', wiz.id, emiley.id )
BloodOath.create( 'emiley takes the lead', branch.id, emiley.id )

BloodOath.create( 'Follower#fellow_members', gate.id, ix.id )



print( "Mwahahaha!" )
ipdb.set_trace()