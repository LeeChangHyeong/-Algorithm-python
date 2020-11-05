#백준 14681번 문제
#https://www.acmicpc.net/problem/14681

a = input()
b = input()

if int(a)<0 and int(b)<0:
    print(3)
elif int(a)<0 and int(b)>0:
    print(2)
elif int(a)>0 and int(b)<0:
    print(4)
else:
    print(1)

