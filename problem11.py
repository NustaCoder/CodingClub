lst1 = input().split()
lst2 = []

for i in range(len(lst1)-1):
    cnt = 0
    for j in range(i,len(lst1)):
        if(lst1[i] > lst1[j]):
            cnt += 1
    lst2.append(cnt)
lst2.append(0)
print(lst2)