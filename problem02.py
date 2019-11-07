import math
a = input()
msg = ""

temp=a.split('.')
k = math.pow(10,len(temp[0])-1)

print(temp)
for i in temp[0]:
    msg+=i+"*"+str(int(k))+"+"
    k/=10

k = 10

for i in temp[1]:
    msg+=i+"/"+str(int(k))+"+"
    k*=10

print(msg[:len(msg)-1])
