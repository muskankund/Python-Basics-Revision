'''Hybrid inheritance is a combination of multiple inheritance and multilevel inheritance. The class is derived from the two classes as in the multiple inheritance. However, one of the parent classes is not the base class. It is a derived class.''' 
'''Hybrid Inheritance combines more than one form of inheritance. It is a blend of more than one type of inheritance'''
class GrandParents(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name


# Inherited or SubClass
class Parents(GrandParents):

    # Constructor
    def __init__(self, name, age):
        GrandParents.__init__(self, name)
        self.age = age

    # To get name
    def getAge(self):
        return self.age


# Inherited or SubClass
class Children(Parents):

    # Constructor
    def __init__(self, name, age, address):
        Parents.__init__(self, name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address


g = Children("riya", 360001, "Rajkot")
print(g.getName(), g.getAge(), g.getAddress())