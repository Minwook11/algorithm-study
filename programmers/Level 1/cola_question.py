# https://school.programmers.co.kr/learn/courses/30/lessons/132267

from math import remainder
from re import A


def solution(a, b, n):
    left, give, take = n, 0, 0
    answer = 0
    while True:
        val, remainder = divmod(left, a)

        give = val * a
        take = val * b
        if val > 0:
            answer += take
        left = left - give + take
        
        if left < a:
            break

    return answer

print(solution(3, 1, 20))