'''point class -- A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.'''
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY): #init function 

        self.x = initX
        self.y = initY

    def getX(self): #The getX method, when invoked, will return the value of the x coordinate.
        return self.x

    def getY(self): #The getY method, when invoked, will return the value of the y coordinate.
        return self.y


p = Point(int(input()),int(input())) #calling the class
print("x coordinate is :",p.getX()) #printing x coordinate
print("y coordinate is:",p.getY()) #printing y coordinate
