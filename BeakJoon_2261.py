#백준 2261번 문제
#https://www.acmicpc.net/problem/2261
#2020-10-16 23:24

import math
n = int(input())
spot=[0 for _ in range(n*2)]

for i in range(0, n*2, 2):
    a,b = map(int, input().split())
    spot[i] = a
    spot[i+1] = b


def cal(a,b,c,d):
    w = (a-c) ** 2 + (b-d) ** 2 
    return w

near = cal(spot[0],spot[1],spot[2],spot[3]) 


for i in range(0, 2*n, 2):
    for j in range(4, 2*n, 2):
        if i < j:
            if cal(spot[i],spot[i+1],spot[j],spot[j+1]) < near:
                near = cal(spot[i],spot[i+1],spot[j],spot[j+1])
                print(near)

