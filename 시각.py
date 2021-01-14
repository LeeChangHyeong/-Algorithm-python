n = int(input())
count = 0
for i in range(n+1):  # 시
    for j in range(60):  # 분
        for k in range(60):  # 초
            if '3' in str(i) + str(j) + str(k):  # 시분초를 문자열로 나열한 후 3이 포함되어 있으면
                count = count + 1  # count에 1을 더함
print(count)
