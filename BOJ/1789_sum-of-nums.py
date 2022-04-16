# link : https://www.acmicpc.net/problem/1789

S = int(input())

step = [1]
while True:
    if sum(step) > S:
        step = step[:-1]
        break
    elif sum(step) == S:
        break
    else:
        step.append(step[-1] + 1)
        
print(len(step))


# 참고한 답안
# s = int(input())
# n = 1
# while n * (n + 1) / 2 <= s:
#     n += 1
# print(n - 1)