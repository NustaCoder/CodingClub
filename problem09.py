#function to check if string is pallindrome or not
def checkPall(a):
    b = a[::-1]
    if(a==b):
        return True
    else:
        return False

#string from user
msg = "aabnayanbbb"
#array or list to store pallindrome words
words = []
cnt = 0

#iterate the loop till there is no characte left in the string
while(len(msg) > 0):
    #finding longest pallindrome string
    temp = msg[:len(msg) - cnt]
    if(checkPall(temp)):
        #add the word in the list
        words.append(temp)
        #remove that word from actual string
        msg = msg.replace(temp,'',1)
        cnt = 0
    else:
        cnt += 1
print(words)
