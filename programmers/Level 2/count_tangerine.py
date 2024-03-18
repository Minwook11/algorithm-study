# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from cgi import test
from collections import Counter

# def solution(k, tengerine):
#     return min([len(list(set(data))) for data in combinations(tengerine, k) if len(data) == k])

def solution(k, tengerine):
    answer = 0
    teng_counter = dict(Counter(tengerine))

    test_dict = dict(sorted(teng_counter.items(), key=lambda x:x[1], reverse=True))

    k_check = 0
    counter = 0
    for _, value in test_dict.items():
        counter += 1
        k_check += value
        if k_check >= k:
            answer = counter
            break

    return answer

print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))