def matches(str1,str2): #defining function as matches with two string arguments
	count=0 #initialize count to 0
	a=len(str1) #length of first string
	b=len(str2) #length of second string
	c=min(a, b) #finding the minimum length in length of both the strings
	for i in range(0, c): #using for loop to count the natches
		if str1[i]==str2[i]: #if condition to check the characters matching in both strings
			count+=1 
	return count #returning the value of the matches in both the strings i.e. count
str1="python" #inputing string 1
str2="path" #inputing string 2
result=matches(str1,str2) # result 
print("the no. Of matches in both the strings are : " ,result) #printing result