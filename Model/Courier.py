from User import User
from Location import Location


class Courier(User):

    locations=[]

    def __init__(self, id, pwd, name, lastname, phone, idDoc, vehicleType, plate, state, dateTime):
        User.__init__(self, id, pwd, name, lastname, phone, idDoc)
        self.vehicleType=vehicleType
        self.plate=plate
        self.state=state
        self.dateTime=dateTime

    def addLocation(self, coordinateX, coordinateY, name):
        newLocation=Location(coordinateX, coordinateY, name)
        Courier.locations.append(newLocation)

    def getVehicleType(self):
        return self.vehicleType

    def setVehicleType(self, vehicleType):
        self.vehicleType=vehicleType

    def getPlate(self):
        return self.plate

    def setPlate(self, plate):
        self.plate=plate

    def getState(self):
        return self.state

    def setState(self, state):
        self.plate=plate

    def getDateTime(self):
        return self.dateTime

    def setDateTime(self, dateTime):
        self.dateTime=dateTime