import sqlalchemy as db

class Order:
    '''
    engine = db.create_engine('sqlite:///users.sqlite3')
    con = engine.connect()
    '''
    
    def __init__(self, senderLoc, destLoc, state, description):
        self.senderLoc=senderLoc
        self.destLoc=destLoc
        self.state=state
        self.description=description

    def getSenderLoc(self):
        return self.senderLoc

    def setSenderLoc(self, senderLoc):
        self.senderLoc=senderLoc

    def getDestLoc(self):
        return self.destLoc

    def setDestLoc(self, destLoc):
        self.destLoc=destLoc

    def getState(self):
        return self.state

    def setState(self, state):
        self.state=state

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description=description