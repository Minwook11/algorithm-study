# link : https://www.acmicpc.net/problem/16435

count, length = map(int, input().split())
furuits = list(map(int, input().split()))

furuits.sort()

for furuit in furuits:
    if furuit <= length:
        length += 1
    else:
        break
print(length)