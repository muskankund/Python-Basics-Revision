#input values of three variables 
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
print("before swapping a =",a,", b =",b,", c =",c)
# Store sum of all in a 
a=a+b+c 
# After this, b has value of a 
b=a-(b+c) 
 # After this, c has value of b 
c=a-(b+c) 
# After this, a has value of c 
a = a-(b+c) 
print("After swapping a =",a,", b =",b,", c =",c) 

