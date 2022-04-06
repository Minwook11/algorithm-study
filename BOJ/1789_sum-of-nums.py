# link : https://www.acmicpc.net/problem/1789

S = int(input())

answer, step = 0, [1]
while True:
    answer += step[-1]
    if answer >= S:
        break
    else:
        step.append(step[-1] + 1)
        
print(answer)
print(len(step) - 1)