'''the __init__ method is used when the class is called to initialize the instance, while the __call__ method is called when the instance is called'''
#The _init_ is used to initialise newly created object, and receives arguments used to do that:
class Foo:
    def __init__(self, a, b, c):
        # ...

x = Foo(1, 2, 3) # __init__
#The _call_ implements function call operator.
class Foo:
    def __call__(self, a, b, c):
        # ...

x = Foo()
x(1, 2, 3) # __call__
