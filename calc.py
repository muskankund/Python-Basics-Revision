i=[1,2,3,4,5,6]
n=int(input())
a=int(input())
b=int(input())
for n in range(i):
	if n==i[0]:
		print(a+b)
	elif n==i[1]:
		print(a-b)
	elif n==i[2]:
		print(a*b)
	elif n==i[3]:
		print(a//b)
	elif n==i[4]:
		print(a%b)
	else n==i[5]:
		print("")
else:
	print('Invalid Operation')