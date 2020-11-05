t = int(input())

sum = [0 for _ in range(t)]

for j in range(t):
    h,w,n = map(int, input().split())
    if n<=h:
        sum[j]=(n*100)+1
    elif h==1:
        sum[j] = 100+n
    elif n%h==0 and h != 1:
        sum[j]=int(h)*100+w
    else:
        sum[j]=(int(n/h)+1)+100*int(n%h)

for i in range(t):
    print(sum[i])