#Import GQL Database Library
from google.appengine.ext import db

#User Database
class Users(db.Model):
    user = db.StringProperty(required=True)          #Username
    pword = db.StringProperty(required=True)         #User Password
    email = db.StringProperty(required=True)         #Email (Required, Except for Genesis Accs)
    handler = db.StringProperty(required=True)       #Gamer Handler (Will Be Set to Username Initially)
    summoner = db.StringProperty(required=False)     #User League of Legends Summoner
    gender = db.BooleanProperty(required=True)       #Checks if Girl or Guy
    faithful = db.BooleanProperty(default=True)      #Checks If User is Loyal
    achievments = db.ListProperty(int, default=None) #List of User Achievments IDs
    genesis = db.BooleanProperty(default=False)      #Genesis Account
    joined = db.DateTimeProperty(auto_now_add=True)  #Creation Date

#Classified Database
##class Key(db.Model):
##    genesis = db.StringProperty(default="genesis")
##    SECRET = db.StringProperty(default="wallace")
