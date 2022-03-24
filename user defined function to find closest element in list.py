def closest(n):
        x=int(input("enter the no. of elements of list"))
        list_ =[]
        list2 =[]
        i=0
        for i in range(1,x):
            list_.append(int(input()))
        list_.sort()
        print(list_)
        for i in list_:
            if i<n:
                list2.append(i)
        print(list2[-1])
closest(8)