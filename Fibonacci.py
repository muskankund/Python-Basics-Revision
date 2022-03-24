n=int(input("enter the no. of terms"))
a=1
b=1
count=0
if n == 1:
   print(a)
else:
   while count < n:
       print(a)
       x=a+b
       a=b
       b=x
       count+=1