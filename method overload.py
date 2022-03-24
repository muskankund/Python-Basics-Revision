class python: #class as python
	def __init__(self, name, value): #init function with two positional arguments name and value
		self.name = name
		self.value = value
	def __abs__(self): #defining abs function to return vector
		return (self.name ** 2 + self.value ** 2) ** 0.5
vector = python(3, 4) #calling class with two arguments name and value
y=abs(vector) #calling function to grt vector
print( 'the vector is :',y) #printing vector