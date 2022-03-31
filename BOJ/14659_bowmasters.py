# link : https://www.acmicpc.net/problem/14659

master_num = int(input())
heights = list(map(int, input().split()))

answer = 0
for i in range(len(heights) - 1):
    count = 0
    for j in range(i + 1, len(heights)):
        if heights[i] > heights[j]:
            count += 1
        else:
            break

    if answer < count: answer = count
    if answer == master_num - 1: break

print(answer)