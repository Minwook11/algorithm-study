# link : https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    if K == 0:
        return answer

    heapq.heapify(scoville)
    while(True):
        min_val = heapq.heappop(scoville)

        if min_val > K:
            break

        if len(scoville) == 0 and min_val < K:
            answer = -1
            break

        next_min_val = heapq.heappop(scoville)
        heapq.heappush(scoville, int(min_val + (next_min_val * 2)))
        answer += 1

    return answer
