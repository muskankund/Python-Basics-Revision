#input the no. of emails
n = int(input("how many email addresses:"))
email = []
#for loop to enter email addresses
for i in range(0 , n):
    x = input("Enter the email{} :-".format(i))
    email.append(x)
    count = 0
    c = "@prof.sharda.edu"
    e = "@ug.sharda.ac.in"
    #for loop to check that email is of student or of professor
    for i in email:
        d = i[-16:]
        if c == d:
            count += 1
        elif e == d:
            continue
        else:
            print("ERROR!!!")
    if count == 0:
        print("All are students.")
    else:
        print("All are not student.")