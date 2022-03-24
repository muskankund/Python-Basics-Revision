names=[]
n=int(input("how many names you want to enter"))
for i in range(n):
	print(i+1,"enter name")
	names.append(input())
s=set(names)
print(s)