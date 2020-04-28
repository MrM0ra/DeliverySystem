from User import User
import random

class Enterprise:

    users=[]

    def __init__(self, name):
        self.name=name

    def getNombre(self):
        return self.name

    def setName(self, name):
        self.name=name

    def setProfitType(self, profitType):
        return 0


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

    def filterCourier(self):
        couriers = []
        for i in Enterprise.users:
            if i.type('Courier') and i.getState() == "disponible":
                couriers.append(i)
        return couriers

    def assignOrder(self, order):
        couriers = filterCourier(self)
        random_courier = random.choices(couriers)
        random_courier.getOrders.appened(order)