# https://school.programmers.co.kr/learn/courses/30/lessons/12927


# def solution(n, works):
#     if len(works) > 1:
#         while True:
#             abs_remain_list = sorted(list(set(works)), reverse=True)

#             if len(abs_remain_list) > 1:
#                 largest, larger = abs_remain_list[0], abs_remain_list[1]
#                 worked = largest - larger
#             else:
#                 largest, larger = abs_remain_list[0], abs_remain_list[0]
#                 worked = 1

#             if largest == 0:
#                 break

#             if n >= worked:
#                 n -= worked
#                 works[works.index(largest)] -= worked
#             else:
#                 works[works.index(largest)] -= n

#             if n == 0:
#                 break

#         return sum([i**2 for i in works])
#     else:
#         remain = works[0] - n if works[0] > n else 0

#         return remain ** 2

import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    
    return sum([w ** 2 for w in works])

print(solution(4, [4,3,3]))