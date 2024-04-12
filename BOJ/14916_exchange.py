# link : https://www.acmicpc.net/problem/14916

exchange = int(input())

answer = 100000
f_count = 0
while True:
    if f_count * 5 > exchange:
        break
    left_exchange = exchange - (5 * f_count)

    value, remain = divmod(left_exchange, 2)

    if remain == 0:
        if answer > value + f_count:
            answer = value + f_count
    
    f_count += 1

answer = answer if answer != 100000 else -1

print(answer)