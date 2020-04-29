from Model.Order import Order
from Model.User import User
import random
from tkinter import messagebox

class Enterprise:

    users=[]
    stackOrder=[]
    knowAorder =[]

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
        self.assignOrder(self,theOrder)

    def addUser(self, id, pwd, name, lastname, phone, idDoc):
        newUser=User(id, pwd, name, lastname, phone, idDoc)
        Enterprise.users.append(newUser)

    def findUser(self, username):
        for i in Enterprise.users:
            if i.getName() == username:
                return i

    def knowAssignedOrders(self, order ):
        if order.getState() == "Asignada" or order.getState() == "En camino" :
            self.knowAorder.append(order)
            messagebox.showinfo(message="Esta orden ya esta asignada", title="Atención")
        if order.getState() =="No Asignada":
            messagebox.showinfo(message="Esta orden no a sido asignada", title="Atención")
        else:
            messagebox.showinfo(message="Ha ocurrido un error, por favor intente de nuevo,", title="Atención")

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
        couriers = self.filterCourier(self)
        random_courier = random.choices(couriers)
        random_courier.getOrders.appened(order)