#Import Library of Functions
from GlobalLib import *

#Define Handler
class GameHandler(Handler):
    def get(self, game):
        game = game.replace('/', '') #Remove "/"
        mainPage = (game=='')
        if(mainPage):
            pass
        else:
            error(game)
            self.render('game.html')
    def post(self, game):
        game = game.replace('/', '') #Remove "/"
        mainPage = (game=='')
        if(mainPage):
            pass
        else:
            week = getWeek()
            error(game)
            pointsQuery = db.GqlQuery('SELECT * FROM Weeks WHERE week=:1', week).get()
            if(pointsQuery==None):
                newWeek = Weeks(week=week, girlPoints=points, boyPoints=points)
                newWeek.put()
            else:
                pointsQuery.girlPoints += point
                pointsQuery.boyPoints += point
