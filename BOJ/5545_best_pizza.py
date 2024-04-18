# link : https://www.acmicpc.net/problem/5545

N = int(input())
A, B = list(map(int,input().split()))
C = int(input())

topping_cal_list = []
for _ in range(N):
    topping_cal_list.append(int(input()))

topping_cal_list.sort(reverse=True)

answer = C / A
for i in range(1, N + 1):
    price = A + (B * i)
    calories = C + sum(topping_cal_list[:i])
    ratio = calories / price

    answer = max(answer, ratio)
    
print(int(answer))