# link : https://www.acmicpc.net/problem/18238

word = input()

start = 'A'
time = 0

for i in word:
    forward = ord(start) - ord(i) + 26 if ord(start) - ord(i) < 0 else ord(start) - ord(i)
    reverse = ord(i) - ord(start) + 26 if ord(i) - ord(start) < 0 else ord(i) - ord(start)

    time += min(forward, reverse)
    start = i

print(time)