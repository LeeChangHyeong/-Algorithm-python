n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))
# 이진탐색을 위해 start, end 지정
start = 0
# 가장 긴 떡의 길이
end = max(rice_cake)

while (start<=end):
    total = 0
    mid = (start+end)//2
    # 떡들을 하나 씩 뽑아서 mid와 길이를 비교한 다음 떡의 길이가 더 길면 mid를 뺀 값을 total에 저장한다.
    for i in rice_cake:
        if i > mid:
            total = total + i - mid
    # 손님이 원하는 떡의 길이가 더 길때 떡을 더 잘라야한다 (왼쪽 탐색) 
    if total < m:
        end = mid-1
    # 손님이 원하는 떡의 길이보다 떡이 더 길때 (오른쪽 탐색)
    # result를 설정한 이유는 최대한 덜 잘랐을 때의 값이 정답이기 때문에 저장을 해놓는다. 
    else:
        result = mid
        start = mid + 1

print(result)