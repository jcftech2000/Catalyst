#Import Library of Functions
from GlobalLib import *

#Define Handler
class LoginHandler(Handler):
    def get(self):
        self.render('login.html')
    def post(self):
        self.render('login.html')
