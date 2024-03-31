# https://school.programmers.co.kr/learn/courses/30/lessons/131704

import time

def solution(order):
    answer = 0
    sub_belt = []

    for box_item in range(1, len(order) + 1):
        if box_item == order[0]:
            answer += 1
            order.pop(0)
        else:
            if sub_belt:
                if order[0] == sub_belt[-1]:
                    answer += 1
                    sub_belt.pop()
                    order.pop(0)
                else:
                    sub_belt.append(box_item)
            else:
                sub_belt.append(box_item)

    for sub_belt_box, order_box in zip(sub_belt[::-1], order):
        if sub_belt_box == order_box:
            answer += 1
        else:
            break

    return answer

print(solution([5,4,3,2,1]))