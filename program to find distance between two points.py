'''point class -- A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.'''
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY): #init function with three arguments self , initX , initY

        self.x = initX
        self.y = initY

    def getX(self): #getY method simply returns the value of self.x
        return self.x

    def getY(self):  #getY method simply returns the value of self.y
        return self.y

    def distanceFromOrigin(self): #distance from origin method to find distance between self.x and self.y
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point(int(input()),int(input())) #inputing the values of x and y
print('the x coordinate is: ', p.getX()) #printing value of self.x
print('the y coordinate is: ', p.getY()) #printing value of self.y

print('the distance from origin is:', p.distanceFromOrigin())  #printing distance
