N=int(input("Total number of rows"))
for i in range(1, N+1) : 
	for j in range(1, N+1) : 
		if (i == 1 or i == N) : 
			print("#", end = "")
		else:
			if (j == 1 or j == N) : 
				print("*", end = "")    
			else :
				print(" ", end = "")
	print()
          