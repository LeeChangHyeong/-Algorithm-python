n, m, k = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort(reverse = True)

result = 0

while True:
    for i in range(k):
        if m == 0:
            break

        result = result + n_list[0]
        m = m - 1
    if m == 0:
        break
    result = result + n_list[1]
    m = m - 1

print(result)






