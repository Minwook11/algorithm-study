# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import queue


def solution(operations):
    d_p_queue = []

    for operation in operations:
        command, value = operation.split()
        value = int(value)

        if command == 'I':
            queue_len = len(d_p_queue)
            if queue_len > 0:
                added_check = False
                for i in range(queue_len):
                    if value <= d_p_queue[i]:
                        d_p_queue.insert(i, value)
                        added_check = True
                        break
                if not added_check:
                    d_p_queue.append(value)
            else:
                d_p_queue.append(value)

        elif command == 'D':
            if len(d_p_queue) > 0:
                if value == -1:
                    d_p_queue.pop(0)
                else:
                    d_p_queue.pop(-1)
            else:
                pass
        else:
            pass

    return [d_p_queue[-1], d_p_queue[0]] if len(d_p_queue) > 1 else [0, 0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))