#백준 8958번 문제
#https://www.acmicpc.net/problem/8958
score = 0
cnt = 0
n = int(input())
list=[]
for i in range(n):
    ox = input()
    for j in range(len(ox)):
        if ox[j] == 'O':
            cnt = cnt + 1
            score = score + cnt
        elif ox[j] == 'X':
            cnt = 0
    list.append(score)
    score=0
for i in range(n):
    print(list[i])
