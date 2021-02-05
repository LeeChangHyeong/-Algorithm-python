n = int(input())
# 모든 식량 창고 정보
array = list(map(int, input().split()))
# 계산 결과를 기록하기 위한 테이블 초기화
d = [0] * 100
# d의 개념이 d[3]이면 3번째 창고까지 들고 갈 수 있는 가장 많은 식량의 양이다.
# 그러므로 d[0]에는 당연히 array[0], d[1]은 나란히 있는 두개의 창고를 못 털어가니 array[0]과 array[1]중 더 큰 값을 넣어준다.
d[0] = array[0]
d[1] = max(array[0], array[1])

# 모든경우에 대해서 값을 구함
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+ array[i])

print(d[n-1])
