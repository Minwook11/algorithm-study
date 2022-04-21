# link : https://www.acmicpc.net/problem/9237

from random import seed


seedling_count = int(input())
grow_period = list(map(int, input().split()))

grow_period.sort(reverse=True)

day, invite_day = 1, 1
for period in grow_period:
    if period + day > invite_day: invite_day = period + day
    day += 1

print(invite_day + 1)