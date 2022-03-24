#else clause
# Function which returns a/b 
def AbyB(a , b): 
	try: 
		c = ((a+b) / (a-b)) 
	except ZeroDivisionError: 
		print ("a/b result in 0")
	else: #else clause
		print (c)
print(AbyB(2.0, 3.0) )
print(AbyB(3.0, 3.0) )