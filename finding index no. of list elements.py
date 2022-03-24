l=[]
n=int(input("how many elements you want to enter"))
for i in range(n):
	print(i+1,"enter element")
	l.append(input())
i=0
x=input("enter the element you want to search")
print('index no. are:')
for i in range(n):
	if l[i]==x:
		print(i)