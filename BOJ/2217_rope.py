# link : https://www.acmicpc.net/problem/2217

rope_num = int(input())
ropes = []
for _ in range(rope_num):
    ropes.append(int(input()))
ropes.sort(reverse=True)

answer = 0
for i in range(len(ropes)):
    temp = ropes[i] * (i+1)
    if temp > answer: answer = temp

print(answer)