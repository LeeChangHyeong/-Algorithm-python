n, m = map(int, input().split())
answer = 0 #가장 작은 수 중 가장 큰 수
list_min = 0 #리스트에서 가장 작은 값 
for i in range(n): #열의 갯수만큼 리스트를 받음
    list_n = list(map(int, input().split()))
    list_min = min(list_n) #파이썬 내장함수인 min을 사용해서 리스트에서 가장 작은 수를 찾고 저장
    if answer < min(list_n): #answer함수의 값이랑 min값을 비교하여 min 값이 answer의 값보다 크면
        answer = list_min #answer에 min값 저장

print(answer)
