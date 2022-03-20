# link : https://www.acmicpc.net/problem/16756

n = int(input())
numbers = list(map(int, input().split()))

answer = None
for i in range(n - 1):
    temp_interval = abs(numbers[i] - numbers[i+1])

    if not answer:
        answer = temp_interval
        continue
    if answer > temp_interval:
        answer = temp_interval

print(answer)