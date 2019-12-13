n = int(input())
box = list()
cnt = 0
for i in range(n):
    a, b = map(int,input().split())
    box.append([a,b,0])

for i in range(len(box)):
    temp = 0
    for j in range(i+1,len(box)):
        st1 , st2 = box[i][0], box[j][0]
        ed1 , ed2 = box[i][1], box[j][1]
        if((ed1>st2 and ed1<ed2) or (ed2>st1 and ed2<ed1)):
            temp += 1
    box[i][2] = temp
    if(temp > cnt):
        cnt = temp
for i in range(len(box)):
    if cnt is box[i][2]:
        box.pop(i)
        break
for i in range(len(box)):
    print("(",box[i][0],",",box[i][1],")")
    
