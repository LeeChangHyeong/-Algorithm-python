#백준 15650번 문제
#https://www.acmicpc.net/problem/15650

n,m = map(int,input().split())
numbers = [i+1 for i in range(n)] # 1 2 3 4
is_number = [0 for _ in range(m)] # 0 0
 
def dfs(idx,next):
    print(idx,'     ',next)

    if idx >= m: 
        print(*is_number) 
        return
    for i in range(next,n):
            is_number[idx] = numbers[i]
            dfs(idx+1,i+1) 
         
            
dfs(0,0)