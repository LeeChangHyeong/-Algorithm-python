n = int(input())
array = list(map(int, input().split()))
# array를 오름차순으로 정렬
array.sort() 
m = int(input())
# 손님이 찾는 부품들 리스트
x = list(map(int, input().split()))

# 반복문으로 이진탐색 함수 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# 부품 번호를 하나씩 확인
for i in x:
    answer = binary_search(array, i, 0, n-1)
    if answer != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')