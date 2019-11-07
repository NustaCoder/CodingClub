arr = [10,15,3,7]
k = int(input())
flg = 1

#normal method
for i in range(len(arr)):
    temp = int(arr[i])
    for j in range(i+1,len(arr)):
        t = temp + int(arr[j])
        if(t == k):
            print(temp," + ",arr[j])
            flg = 0
            break
if(flg):
    print("null")
