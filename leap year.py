x=int(input("enter year"))
result= "leap year" if x%400==0 else "leap year" if x%4==0 else "non leap year"
print(result)