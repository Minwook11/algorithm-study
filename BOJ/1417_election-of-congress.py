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
    print(supporters)
    for supporter in supporters:
        if current > supporter:
            break
        else:
            step = ((current + supporter) // 2) + 1 - current
            answer += step
            current += step

    print(answer)