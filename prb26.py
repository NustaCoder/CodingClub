a = [1,2,3,4,5,6]
b = [1,2,3,4,5]
l = []
i = 0
if len(a)%2!=0:
    a.append(0)
while i<len(a):
    c = a[i] + a[i+1]
    l.append(c)
    i+=2
print(l)