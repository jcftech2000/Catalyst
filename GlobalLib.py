from Handler import *
from CatalystDB import *
from logging import error
from hmac import HMAC
from urllib import urlencode
from urllib2 import urlopen
from urllib2 import urlparse
from json import loads
from random import random
from datetime import datetime

#Store Secret Variables (Later Use "Key" Database)
SECRET = 'wallace'  #Password Hashing
GENESIS = 'wallace' #Used for Genesis Accounts

def getWeek():
    return datetime.now().isocalendar()[1]

#Hashing for Cookie Security & Validation
def encodeCookie(uid, pword):
    return HMAC(str(pword), str(HMAC(SECRET, uid).hexdigest())).hexdigest()

#Generate Cookie String for addCookie()
def genCookie(uid, pword):
    params = {}
    params['user_id'] = uid
    params['token'] = encodeCookie(uid, pword)
    error(urlencode(params))
    encodeParams = urlencode(params)
    cookie = 'session_id='+encodeParams+'; path=/'
    return cookie

#Parse and Validate Cookies
def parseCookie(cookie):
    parsed = urlparse.parse_qs(cookie)
    if(parsed.has_key('user_id') and parsed.has_key('token')):
        uid = parsed['user_id'][0]
        token = parsed['token'][0]
        userQuery = Users.get_by_id(int(uid))
        if(userQuery != None):
            pword = userQuery.pword
            if(token==encodeCookie(uid, pword)):
                return True
    return False

def hashPw(pword):
    return HMAC(SECRET, pword).hexdigest()
