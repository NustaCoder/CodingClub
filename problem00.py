msg = input()

for i in msg:
    a = ord(i)
    if(a>96 and a<122):
        print(a-96,end=' ')
