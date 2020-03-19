import itertools
def sub_lists(list1): 
    temp = []
    for i in range(len(list1)):
        temp.extend([set(i) for i in itertools.combinations(list1, i+1)])
    return temp

a = [1,2,3,10]
c = 1
b = sub_lists(a)
d = []
for i in b:
    d.append(sum(i))
d.sort()
print(d)
for i in d:
    if c == i:
        c+=1
else:
    print(c)