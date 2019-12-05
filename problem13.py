num = int(input())
a = int(num/2)
if(num%2 != 0):
    for i in range(num):
        for j in range(num):
            if(i==a or j==a):
                print("X",end=" ")
            else:
                print("0",end=" ")    
        print()