from Order import Order


class User:

    orders = []

    def __init__(self, id, pwd, name, lastname, phone, idDoc):
        self.id=id
        self.pwd=pwd
        self.name=name
        self.lastname=lastname
        self.phone=phone
        self.idDoc=idDoc

    def addOrder(self, senderLoc, destLoc, state, description):
        order=Order(senderLoc, destLoc, state, description)
        User.orders.append(order)

    def getOrders(self):
        return User.orders

    def getId(self):
        return self.id

    def setId(self, id):
        self.id=id

    def getPwd(self):
        return self.pwd

    def setPwd(self, pwd):
        self.pdw=pwd

    def getName(self):
        return self.name

    def setName(self, name):
        self.name=name

    def getLastName(self):
        return self.lastname

    def setLastName(self,lastname):
        self.lastname=lastname

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone=phone

    def getIdDoc(self):
        return self.idDoc

    def setIdDoc(self, idDoc):
        self.idDoc=idDoc

    def available(self):
        isAvailable = True
        if len(self.orders) > 1:
            isAvailable = False
        return isAvailable



