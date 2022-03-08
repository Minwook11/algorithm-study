# link : https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    user_left = len(stages)
    for stage in range(1, N + 1):
        user_count = stages.count(stage)

        if user_count == 0:
            answer.append((stage, 0))
        else:
            answer.append((stage , user_count / user_left))
            user_left -= user_count

    res = sorted(answer, key=lambda x : x[1], reverse = True)

    return [ i[0] for i in res ]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))