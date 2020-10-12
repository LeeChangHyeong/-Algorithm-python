#백준 11047번 문제
#https://www.acmicpc.net/problem/11047

a,money = map(int,input().split())
value = [0 for _ in range(a)]
for i in range(a):
    value[i] = int(input())

def answer(a,money):
    temp=0
    count=0
    for i in range(a-1, -1, -1):
         temp = int(money/value[i])
         money = money - value[i]*temp
         count = count + temp
         if money == 0:
             return count


print(answer(a,money))