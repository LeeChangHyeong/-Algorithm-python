a, b, v = map(int, input().split())

s = 0
count = 0

while(True):
    s = s + a 
    if(s>=v):
        count = count+1 
        print(count)
        break
    s = s - b 
    count = count+1 