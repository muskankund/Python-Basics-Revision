array1=[]
array2=[]
n= int(input("enter the no.  of elements of array1:"))
p=int(input("enter the no.  of elements of array2:"))
i=0
t=0
print("the original arrays are :" )
for i in range(n):
   array1.append(input())
print("array1=" ,array1)
for t in range(p):
    array2.append(input())
print("array2=" ,array2)
result = list(filter(lambda x: x in array1, array2 ))
print("\n The intersection of the arrays are :" , result)