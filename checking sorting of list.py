def is_sorted(list):    
    for i in range(1,len(list)):
        if list[i - 1] > list[i]:
           return False
    return True
numbers =[2,3,10,12,15,16]
result = is_sorted(numbers)
print(result)