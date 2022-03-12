# link : https://www.acmicpc.net/problem/22864

A, B, C, M = map(int, input().split())

worked, fatigue = 0, 0

for _ in range(24):
    if M >= fatigue and M >= fatigue + A:
        fatigue += A
        worked += B
    else:
        fatigue -= C
        if fatigue < 0:
            fatigue = 0

print(worked)