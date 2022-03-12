# link : https://www.acmicpc.net/problem/14720

n = int(input())
milk_order = map(int, input().split())

current_step = 0
answer = 0

for milk in milk_order:

    if milk == current_step:
        answer +=1
        current_step += 1
        if current_step > 2: current_step = 0

print(answer)