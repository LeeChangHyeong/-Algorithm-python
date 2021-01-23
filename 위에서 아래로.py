n = int(input())
array = []

for i in range(n): 
    array.append(input())

# 파이썬 라이브러리 이용 
# (중요!) sorted는 원래 오름차순이지만 reverse = True를 사용시 내림차순으로 변경된다.
array = sorted(array, reverse = True) 

for i in array:
    print(i, end=' ')