# link : https://programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations

def solution(k, dungeons):
    max_count = len(dungeons)
    all_trying_case = list(permutations(dungeons))
    clear = 0
    for single_case in all_trying_case:
        current = k
        temp_clear = 0
        for step in single_case:
            if step[0] <= current and step[1] <= current:
                current -= step[1]
                temp_clear += 1
            else:
                break
        
        if temp_clear == max_count:
            clear = temp_clear
            break
        
        if temp_clear > clear:
            clear = temp_clear
    return clear

print(solution(80, [[80,20], [50,40], [30,10]]))

# Other programmer's solution -- Most simpliest solution
# solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])