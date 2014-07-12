#Import Library of Functions
from GlobalLib import *

#Define Handler
class CreateHandler(Handler):
    def get(self):
        self.render('create.html')
    def post(self):
        genesis = (self.request.get('genesis')==GENESIS) #Check for Genesis Account
        account = {} #Initialize New Account Object
        #Get all POST parameters
        name = self.request.get('uname')
        pword = self.request.get('pass')
        email = self.request.get('email')
        gender = self.request.get('gender')
        #Check if Valid User
        userCheck = db.GqlQuery('SELECT * FROM Users WHERE user=:1', name)
        emailCheck = db.GqlQuery('SELECT * FROM Users WHERE email=:1', email)
        if(userCheck.get()==None and emailCheck.get()==None):
            account['user'] = name
            account['pword'] = hashPw(pword)
            account['email'] = email
            account['handler'] = account['user']
            account['gender'] = (gender=='girl')
            account['genesis'] = genesis
            error(genesis)
            newUser = Users(**account)
            newUser.put()
        else:
            self.render('create.html')
