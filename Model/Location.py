

class Location:

    def __init__(self, coordinateX, coordinateY, name):
        self.coordinateX=coordinateX
        self.coordinateY=coordinateY
        self.name=name

    def getCoordinateX(self):
        return self.coordinateX

    def setCoordinateX(self, coordinateX):
        self.coordinateX=coordinateX

    def getCoordinateY(self):
        return self.coordinateY

    def setCoordinateY(self, coordinateY):
        self.coordinateX=coordinateY

    def getName(self):
        return self.name

    def setName(self, name):
        self.name=name