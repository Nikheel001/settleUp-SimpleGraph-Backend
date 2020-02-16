from collections import defaultdict


class User:

    __slots__ = ('__owes', '__owed', '__id', '__name', '__no')

    def __init__(self):
        self.__owes = defaultdict(float)
        self.__owed = 0
        self.__id = ''
        self.__name = ''
        self.__no = ''
        self.__group = []

    def __set_group(self, group):
        if not type(group)==list :
            raise TypeError('Cell number should be correct')
        self.__group = group
    
    def __get_group(self): return self.__group

    def __del_group(self): print("Not allowed")
    Groups = property(__get_group, __set_group, __del_group, 'List of groups where user is a member')

    def __set_no(self, no):
        if not (type(no)==str and len(no)==10):
            raise TypeError('Cell number should be correct')
        self.__no = no
    
    def __get_no(self): return self.__no

    def __del_no(self): print("Not allowed")
    CellNo = property(__get_no, __set_no, __del_no, 'Cell number of user')

    def __set_name(self, name):
        if not type(name) == str:
            raise TypeError('User name should be string')
        self.__name = name

    def __get_name(self): return self.__name

    def __del_name(self): print("Not allowed")
    Name = property(__get_name, __set_name, __del_name, 'UserName')

    def __set_owed(self, owed):
        if type(owed) not in [float, int]:
            raise TypeError('Owed money must be number')
        self.__owed = owed

    def __get_owed(self): return self.__owed

    def __del_owed(self): print("Not allowed")
    Owed = property(__get_owed, __set_owed, __del_owed, 'OwedMoney')

    def __set_owes(self, owes):
        if not type(owes) == dict:
            raise TypeError('Error retriving owes information')
        for key, val in owes:
            self.__owes[key] = val
        # self.__owes = owes

    def __get_owes(self): return self.__owes

    def __del_owes(self): print("Not allowed")
    Owes = property(__get_owes, __set_owes, __del_owes, 'MoneyOwed to others')

    def __get_id(self): return self.__id

    def __set_id(self, ObjId): self.__id = ObjId

    def __del_id(self): print("Invalid")
    ObjectId = property(__get_id, __set_id, __del_id, 'ObjectId of user')

    def __call__(self, to, money):
        self.__owes[to] += money

    def __repr__(self):
        return str(self.userAsDict())

    def owes_to(self):
        return set(self.__owes.keys())

    def owedMoney(self, to):
        return self.__owes[to]

    def pay(self, to, money):
        self.__owes[to] -= money
        if self.__owes[to] == 0:
            del self.__owes[to]

    def __len__(self):
        return len(self.__owes)

    def userAsDict(self):
        '''
        represent User as Dictionary(or Json object)
        Groups not mentioned
        '''
        return {'name': self.Name, 'owed': self.Owed, 'owes': self.Owes, 'CellNumber': self.CellNo}

    @classmethod
    def verifyCellNo(cls, no):
        '''
        verify weather no already exists in db
        pin verification from user's cell
        returns true or false
        '''
        return True

    @classmethod
    def fromDict(cls, usr):
        '''
        Initilize User object from given dictionary(or Json)
        '''
        x = User()
        x.ObjectId = usr['_id']
        x.Name = usr['name']
        x.Owed = usr['owed']
        x.Owes = usr['owes']
        x.CellNo = usr['no']
        x.Groups = usr['groups']
        return x
