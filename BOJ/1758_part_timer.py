# https://www.acmicpc.net/problem/1758

N = int(input())

tip_list = []
for _ in range(N):
    tip_list.append(int(input()))

tip_list.sort(reverse=True)

answer = 0
for idx, tip in enumerate(sorted(tip_list, reverse=True)):
    tip_cal = tip - idx
    if tip_cal > 0:
        answer += tip_cal
    else:
        break

print(answer)