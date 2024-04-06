# link : https://www.acmicpc.net/problem/11047

coin_count, target = list(map(int,input().split()))

coin_list = []

for _ in range(coin_count):
    coin_list.insert(0, int(input()))

answer = 0
for coin in coin_list:
    if target == 0:
        break

    val, remain = divmod(target, coin)
    if val > 0:
        target -= coin * val
        answer += val

print(answer)