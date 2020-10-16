#백준 1541번 문제
#https://www.acmicpc.net/problem/1541
#2020-10-14 22:09

equation = input().split('-')
sum = 0
for i in equation[0].split('+'):
    sum = sum + int(i)

for i in equation[1:]:
    for j in i.split('+'):
        sum = sum - int(j)

print(sum)