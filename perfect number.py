#for loop for range of n
for n in range (1 , 10000):
	#initialise sum to 0
    sum =0
    #for loop for range of i to check divisors of n
    for i in range(1 , n):
    	#if condition to check divisors of n
        if n % i ==0:
            sum += i
    if sum == n:
        print(n)