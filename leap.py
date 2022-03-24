#input year 
x=int(input("enter the year"))
#if condition to check that year is greater than 1600 or not
if x<1600:
	print("year is not valid")
else:
	#if else condition for checking leap year
	if x%4==0:   
		if x%100==0:
			if x%400==0:
				print(x,"is a leap year")
			else:
				print(x,"is not a leap year")
		else:
			print(x,"is a leap year")
	else:
		print(x,"is not a leap year")