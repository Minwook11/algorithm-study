# link : https://www.acmicpc.net/problem/1417

candidates = int(input())
supporters = []
for _ in range(candidates):
    supporters.append(int(input()))
    
if candidates == 1:
    print(0)
else:
    answer = 0
    current = supporters.pop(0)
    supporters.sort(reverse=True)
    while True:
        if supporters[0] >= current:
            current += 1
            supporters[0] -= 1
            answer += 1
            supporters.sort(reverse=True)
        else:
            break
        
    print(answer)