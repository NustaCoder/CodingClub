msg = "azc"
brr = [i-i for i in range(26)]
flg = 0
for i in msg:
    a = ord(i) - 97
    brr[a]+=1
    if(brr[a]==2):
        print(chr(a+97))
        flg = 0
        break
    flg += 1
if(flg > 1):
    print("null")
