from Model.Order import Order
from Model.User import User


class Enterprise:

    users=[]
    stackOrder=[]

    def __init__(self, name):
        self.name=name

    def getNombre(self):
        return self.name

    def setName(self, name):
        self.name=name

    def setProfitType(self, profitType):
        return 0

    def addOrder(self, idUser, senderLoc, destLoc, state, description):
        theOrder = Order(senderLoc,destLoc,state,description)
        Enterprise.stackOrder.append(theOrder)
        i = 0
        found = False
        while(i<len(Enterprise.users) and (not found)):
            if Enterprise.users[i].getId() == idUser:
                found = True
                Enterprise.users[i].getOrders().append(theOrder)
            i = i+1

    def addUser(self, id, pwd, name, lastname, phone, idDoc):
        newUser=User(id, pwd, name, lastname, phone, idDoc)
        Enterprise.users.append(newUser)

    def findUser(self, username):
        for i in Enterprise.users:
            if i.getName() == username:
                return i

    def modifyUser(self):
        return 0

    def deleteUser(self):
        return 0
