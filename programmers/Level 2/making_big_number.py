# link : https://programmers.co.kr/learn/courses/30/lessons/42883

import itertools

def solution(number, k):
    temp_res = list(itertools.combinations(list(number), len(number) - k))
    temp_res.sort(reverse=True)

    return ''.join(temp_res[0])

print(solution("4177252841", 4))

# Other programmer's solution -- Reference answer
# def solution(number, k):
#     answer = []
    
#     for num in number:
#         while k > 0 and answer and answer[-1] < num:
#             answer.pop()
#             k -= 1
#         answer.append(num)
        
#     return ''.join(answer[:len(answer) - k])