n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum = sum + min(A) * max(B)
    A.remove(min(A))
    B.remove(max(B))

print(sum)



