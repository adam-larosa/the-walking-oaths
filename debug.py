
import ipdb
from lib.walkingdev import session
from lib.models import *

town = session.query( Cult ).first()


print( "Mwahahaha!" )
ipdb.set_trace()