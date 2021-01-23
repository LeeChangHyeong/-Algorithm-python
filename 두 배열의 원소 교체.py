n, k = map(int, input().split())  # n과 k 입력받기

a = list(map(int, input().split()))  # a list 입력받기
b = list(map(int, input().split()))  # b list 입력받기


a = sorted(a)  # a list는 오름차순 정렬
b = sorted(b, reverse = True)  # b list는 'reverse = True'를 사용해 내림차순으로 정렬

for i in range(k):  # k번 바꿔치기 가능하니 k만큼 반복

    #  정렬을 했다고 a와b를 무작정 바꾸는게 아닌
    #  a[i]와 b[i]를 비교후 a[i]가 b[i]보다 작을시에만 a[i]와 b[i]를 교체
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

# list a를 다 더한값 출력
print(sum(a))