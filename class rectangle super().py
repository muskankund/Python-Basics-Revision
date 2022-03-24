'''Calling the previously built methods with super() saves you from needing to rewrite those methods in your subclass, and allows you to swap out superclasses with minimal code changes.'''
class Rectangle: #parent class as rectangle
    def __init__(self, length, width): #init function to define length and breadth
        self.length = length
        self.width = width

    def area(self): #to find area
        return self.length * self.width

    def perimeter(self):#to find perimeter
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle): #child class
    def __init__(self, length): #init function to define length of square
        super().__init__(length, length)
square=Square(5) #calling class (giving value of length)
print('AREA OF SQUARE :',square.area())
print('PERIMETER OF SQUARE:',square.perimeter()) 
