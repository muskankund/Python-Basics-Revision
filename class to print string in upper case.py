class IOString():      #class
    def __init__(self):   #init function to define empty string
        self.str1 = ""
        
    def get_String(self):    #defining get string function
  	  self.str1 = input()
  	  
    def print_String(self): #defining print string function
        print("string in upper case is :",self.str1.upper())
        
str1 = IOString() 
str1.get_String() #calling get string function
str1.print_String() #calling print string function