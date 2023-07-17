
import ipdb
from lib.walkingdev import session
from lib.models import *

town = session.query( Cult ).first()

followers = session.query( Follower ).all()

adam = followers[0]

emiley = followers[1]

print( "Mwahahaha!" )
ipdb.set_trace()