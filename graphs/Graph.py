from collections import defaultdict
from users.User import User


class Grpah:

    __slots__ = ('__value', '__id', '__name', '__visit_it')
    __visit_it = set()

    def __init__(self):
        self.__value = defaultdict(User)
        self.__id = ''
        self.__name = ''

    def __set_name(self, name):
        if not type(name) == str:
            raise TypeError('Group name should be string')
        self.__name = name

    def __get_name(self): return self.__name

    def __del_name(self): print("Not allowed")
    Name = property(__get_name, __set_name, __del_name, 'GroupName')

    def __set_value(self, value):
        if not type(value) == dict:
            raise TypeError('Group data should be valid')
        for key, val in value.items():
            self.__value[key] = val

    def __get_value(self): return self.__value

    def __del_value(self): print("Not allowed")
    Value = property(__get_value, __set_value, __del_value, 'Group data')

    def __get_id(self): return self.__id

    def __set_id(self, ObjId): self.__id = ObjId

    def __del_id(self): print("Invalid")
    ObjectId = property(__get_id, __set_id, __del_id, 'ObjectId of group')

    def transaction(self, x, y, money):
        self.Value[x](y, money)

    def process(self, x, y, money):
        if y not in self.Value:
            return
        ychd = set(i for i in self.Value[y].owes_to())
        while ychd:
            i = ychd.pop()
            amt = self.Value[y].owedMoney(i)
            if money > amt:
                money, amt = amt, money
            self.Value[x].pay(y, money)
            self.Value[y].pay(i, money)
            if i != x:
                self.transaction(x, i, money)
                if i not in self.__visit_it:
                    self.__visit_it.add(i)

    def processAll(self):
        self.__visit_it = set(self.Value.keys())
        while self.__visit_it:
            k = self.__visit_it.pop()
            if k not in self.Value:
                continue
            for j in self.Value[k].owes_to():
                self.process(k, j, self.Value[k].owedMoney(j))

    def showNetwork(self):
        print(self.Value)

    def clearGraph(self):
        nodes = set(self.Value.keys())
        while nodes:
            i = nodes.pop()
            if len(self.Value[i]) == 0:
                del self.Value[i]

    def graphAsDict(self):
        return {'name': self.Name, 'value': self.Value}

    @classmethod
    def fromDB(cls, graph):
        x = Grpah()
        x.Name = graph['name']
        x.Value = graph['value']
        x.ObjectId = graph['_id']
        return x
