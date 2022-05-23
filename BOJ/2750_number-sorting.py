# link : https://www.acmicpc.net/problem/2750

count = int(input())

numbers = [ int(input()) for _ in range(count) ]

for number in sorted(numbers):
    print(number)