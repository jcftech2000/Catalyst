#Import Library of Functions
from GlobalLib import *

#Define Handler
class MainHandler(Handler):
    def get(self):
        self.render('landing.html', girls="1.1m", boys="998.7k")
