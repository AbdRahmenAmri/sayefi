import jwt
from config.conf import PRIVATE_KEY

def Decode(tokken):
    return jwt.decode(tokken,PRIVATE_KEY,algorithms=['HS256'])
def Encode(DATA):
    return jwt.encode(DATA,PRIVATE_KEY)