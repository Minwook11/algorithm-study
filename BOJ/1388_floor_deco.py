# link : https://www.acmicpc.net/problem/1388

Y, X = list(map(int, input().split()))

floor = []

for _ in range(Y):
    floor.append(input())

answer = 0
for i in range(Y):
    check_val = 0
    for j in range(X):
        if floor[i][j] == "m":
            check_val += 1
        else:
            if check_val > 0:
                answer += 1
                check_val = 0
    if check_val > 0:
        answer += 1

for i in range(X):
    check_val = 0
    for j in range(Y):
        if floor[j][i] == "l":
            check_val += 1
        else:
            if check_val > 0:
                answer += 1
                check_val = 0
    if check_val > 0:
        answer += 1

print(answer)