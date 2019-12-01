import math
a = input().split()
flag = 0
for i in range(len(a)-1):
    temp = math.fabs(int(a[i])-int(a[i+1]))
    if(temp != 1):
        flag = 1
        break
    else:
        pass
if(flag == 1):
    print("no")
elif(flag == 0):
    print("yes")