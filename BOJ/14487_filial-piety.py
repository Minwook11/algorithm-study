# link : https://www.acmicpc.net/problem/14487

n = input()
prices = list(map(int, input().split()))
print(sum(prices) - max(prices))