arr_temp = input().split()
arr_main = [int(i) for i in arr_temp]

for i in range(len(arr_main)-1):
    a = arr_main[i]
    for j in range(i+1, len(arr_main)):
        b = arr_main[j]
        c = a**2 + b**2
        c = c**0.5
        if c in arr_main:
            print("(%d, %d, %d)"%(a,b, int(c)))   
        else:
            pass     