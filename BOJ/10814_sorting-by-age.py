# link : https://www.acmicpc.net/problem/10814

count = int(input())

users = [ input().split() for _ in range(count) ]
users.sort(key=lambda x: x[0])

for user in users:
    print(int(user[0]), user[1])