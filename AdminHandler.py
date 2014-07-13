#Import Library of Functions
from GlobalLib import *

#Define Handler
class AdminHandler(Handler):
    def get(self):
        genesisQuery = db.GqlQuery('SELECT * FROM Users WHERE genesis=:1', True)
        girlGenesis = 0
        boyGenesis = 0
        for genesisDB in genesisQuery:
            if(genesisDB.gender==True):
                girlGenesis += 1
            else:
                boyGenesis += 1
        self.render('admin.html', genesis=girlGenesis+boyGenesis, girlGenesis=girlGenesis, boyGenesis=boyGenesis)
    def post(self):
        genesis = self.request.get('genesis')
        deleteAll = self.request.get('deleteAll')
        if(genesis==GENESIS):
            genesisOpener = urlopen('http://jaredflores.com/catalyst/GENESIS.json')
            genesisContent = genesisOpener.read()
            genesisUsers = loads(genesisContent)
            genesisID = 0
            genesisDB = []
            genesisAccount = {}
            genesisAccount['genesis'] = True
            for uname in genesisUsers:
                genesisID += 1
                genesisAccount['user'] = genesisAccount['handler'] = uname
                if(genesisID <= 1000):
                    #1000 Female Genesis Accounts
                    genesisAccount['gender'] = True
                elif(genesisID <= 2000):
                    #1000 Male Genesis Accounts
                    genesisAccount['gender'] = False
                else:
                    #Randomly Decide Gender of 1000 Genesis Accounts
                    genesisAccount['gender'] = (round(random())==1)
                genesisDB.append(Users(**genesisAccount))
            db.put(genesisDB)
        elif(deleteAll==GENESIS):
            deleteAccs = []
            for user in db.GqlQuery('SELECT * FROM Users WHERE genesis=:1', True):
                deleteAccs.append(user)
            db.delete(deleteAccs)
