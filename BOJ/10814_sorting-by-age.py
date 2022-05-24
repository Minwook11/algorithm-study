# link : https://www.acmicpc.net/problem/10814

count = int(input())

tuplize = lambda x: (int(x[0]), x[1])
users = [ tuplize(input().split()) for _ in range(count) ]
users.sort(key=lambda x: x[0])

for user in users:
    print(user[0], user[1])