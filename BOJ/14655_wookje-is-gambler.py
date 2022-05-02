# link : https://www.acmicpc.net/problem/14655

coin_count = int(input())

first_round = list(map(int, input().split()))
second_round = list(map(int, input().split()))

result = 0
for first, second in zip(first_round, second_round):
    result += abs(first) + abs(second)

print(result)