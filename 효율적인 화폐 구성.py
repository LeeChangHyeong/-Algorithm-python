n, m = map(int, input().split())
list_n = []
for i in range(n):
    list_n.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

for i in range(n):
    for j in range(list_n[i], m+1):
        print(i)
        print(j)
        if d[j - list_n[i]] != 10001:
            d[j] = min(d[j],d[j - list_n[i]] + 1)

if d[m] == 10001:
    print('-1')
else:
    print(d[m])
