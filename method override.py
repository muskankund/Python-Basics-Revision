#method overriding
'''In Python method overriding occurs simply defining in the child class a method with the same name of a method in the parent class. When you define a method in the object you make the latter able to satisfy that method call, so the implementations of its ancestors do not come in play.'''
class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    def get_value(self):
        return self.value + 1
c=Child()
print(c.get_value())
