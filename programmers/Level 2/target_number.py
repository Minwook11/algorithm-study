# link : https://programmers.co.kr/learn/courses/30/lessons/43165

from itertools import product

def solution(numbers, target):
    num_pair_list = [(x, -x) for x in numbers]
    cal_res = list(map(sum, product(*num_pair_list)))
    
    return cal_res.count(target)

print(solution([1,1,1,1,1,1], 4))

# Other programmer's solution -- Most interested answer
#def solution(n, t):
#    answer = 0
#    for i in range(2**len(n)):
#        tmp = []
#        for j in range(len(n)):
#            if i & (2**j) == 0:
#                tmp.append(n[j])
#            else:
#                tmp.append(-1*n[j])
#        if sum(tmp) == t:
#            answer += 1        
#    return answer
