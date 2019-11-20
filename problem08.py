def findPos(s,st,words,a):
    lst = []
    ed = len(s) - len(st) + 1
    for i in range(ed):
        cnt = 0
        temp = s[i:i+len(st)]
        for j in words:
            if j in temp:
                cnt += 1
        if(cnt == len(words)):
            if(a == 0):
                i -= 18
                i *= (-1)
            lst.append(i)
    return lst

sn = "dogcatcatcodecatdog"
sr = sn[::-1]
words = ['dog','cat']
st = ""
for i in words:
    st += i
#normal string
print(findPos(sn,st,words,1))
#reverse string
print(findPos(sr,st,words,0))