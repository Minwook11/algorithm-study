# link : https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum_q1, sum_q2 = sum(queue1) ,sum(queue2)

    for i in range(300000):
        if sum_q1 == sum_q2:
            return i
        elif sum_q1 > sum_q2:
            item = queue1.popleft()
            queue2.append(item)
            sum_q1, sum_q2 = sum_q1 - item, sum_q2 + item
        else:
            item = queue2.popleft()
            queue1.append(item)
            sum_q1, sum_q2 = sum_q1 + item, sum_q2 - item
    return -1

print(solution([1,1], [1,5]))