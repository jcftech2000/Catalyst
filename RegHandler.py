#Import Library of Functions
from GlobalLib import *

#Define Handler
class RegHandler(Handler):
    def get(self):
        self.render('reg.html')
    def post(self):
        self.render('reg.html')
