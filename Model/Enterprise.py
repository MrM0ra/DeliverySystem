from User import User


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
