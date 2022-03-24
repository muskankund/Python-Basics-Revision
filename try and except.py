# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]    #creating a list with different items

for entry in randomList: #using for loop for access element in the list
    try:   #using try for handling type error
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except: #using except for handling zero division error
        print("Oops!", sys.exc_info()[0], "occured.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)