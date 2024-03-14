# https://school.programmers.co.kr/learn/courses/30/lessons/12914

# 중복순열을 사용해서 도전 - 시간 초과로 인한 오답
# from itertools import product

# def solution(n):
#     if n == 1 or n == 2:
#         return n
#     else:
#         answer = 1
#         skill_set = [1, 2]

#         min_try = n//2 if n % 2 == 0 else n//2 + 1

#         for i in range(min_try, n):
#             P_res = product(skill_set, repeat=i)

#             for P_item in P_res:
#                 answer += 1 if sum(P_item) == n else 0

#     return answer

# 다른 사람 답안 참고 - 피보나치 수열 방식으로 접근
def solution(n):
    if n < 3:
        return n
    else:
        data_ary = [0, 1, 2]

        for idx in range(3, n+1):
            data_ary.append(data_ary[idx-1] + data_ary[idx-2])
        
        return data_ary[n] % 1234567

print(solution(4))