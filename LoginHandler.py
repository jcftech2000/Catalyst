#Import Library of Functions
from GlobalLib import *

#Define Handler
class LoginHandler(Handler):
    def get(self):
        self.render('login.html')
    def post(self):
        uname = self.request.get('uname')
        pword = self.request.get('pass')
        userQuery = db.GqlQuery('SELECT * FROM Users WHERE user=:1', uname).get()
        if(userQuery != None and hashPw(pword)==userQuery.pword):
            pass
        else:
            self.render('login.html')
