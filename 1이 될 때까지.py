n, k = map(int, input().split())
count = 0

def math(n, k): #함수 선언
    global count #전역변수 변경 권한 얻음
    if int(n/k) != 1: #몫이 1이 아니면
        n = int(n/k) #n을 n/k의 몫으로 변환
        count = count + 1 #count에 연산 횟수 1 추가
        if n>=k: #n이 k보다 크거나 같을때
            math(n , k) #재귀함수 사용
        else:
            for i in range(n-1): #n이 1이 될때까지 -1을 해주는 작업
                n = n-1
                count = count + 1 #한번 돌때마다 연산 횟수 추가
    elif int(n/k) == 1: #n/k의 몫이 1이면
        count = count + 1


if n<k: #k가 n보다 작을때
    for i in range(n-1): #n이 1이 될때까지 -1을 해주는 작업
        n = n-1
        count = count + 1
else:
    math(n, k)

print(count)


