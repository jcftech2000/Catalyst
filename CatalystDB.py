#Import GQL Database Library
from google.appengine.ext import db

#User Database
class Users(db.Model):
    user = db.StringProperty(required=True)          #Username
    pword = db.StringProperty(required=False)        #User Password (Required, Except for Genesis Accs)
    email = db.StringProperty(required=False)        #Email (Required, Except for Genesis Accs)
    handler = db.StringProperty(required=True)       #Gamer Handler (Will Be Set to Username Initially)
    summoner = db.StringProperty(required=False)     #User League of Legends Summoner
    gender = db.BooleanProperty(required=True)       #Checks if Girl or Guy
    faithful = db.BooleanProperty(default=True)      #Checks If User is Loyal
    achievments = db.ListProperty(int, default=None) #List of User Achievments IDs
    genesis = db.BooleanProperty(default=False)      #Genesis Account
    points = db.IntegerProperty(default=0)           #User Earned Points
    joined = db.DateTimeProperty(auto_now_add=True)  #Creation Date

#Points Database
class Weeks(db.Model):
    week = db.IntegerProperty(required=True)
    girlPoints = db.IntegerProperty(required=True)
    boyPoints = db.IntegerProperty(required=True)

#Classified Database
##class Key(db.Model):
##    genesis = db.StringProperty(default="wallace")
##    SECRET = db.StringProperty(default="wallace")
