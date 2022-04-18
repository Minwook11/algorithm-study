# link : https://www.acmicpc.net/problem/2217

rope_num = int(input())
ropes = []
for _ in range(rope_num):
    ropes.append(int(input()))
ropes.sort(reverse=True)

answer = ropes[0]
for i in range(1, len(ropes)):
    target = ropes[:i]
    available = min(target) * len(target)
    
    if available > answer:
        answer = available
        
print(answer)