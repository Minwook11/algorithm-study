# link : https://www.acmicpc.net/problem/5585

exchange = 1000 - int(input())

answer = exchange // 500
exchange = exchange % 500

answer += exchange // 100
exchange = exchange % 100

answer += exchange // 50
exchange = exchange % 50

answer += exchange // 10
exchange = exchange % 10

answer += exchange // 5
exchange = exchange % 5

answer += exchange // 1

print(answer)