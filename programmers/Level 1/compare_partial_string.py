# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    t_len, p_len = len(t), len(p)

    for i in range(t_len - p_len + 1):
        flag = True if int(t[i:(i+p_len)]) <= int(p) else False
        if flag:
            answer += 1

    return answer

print(solution("500220839878", "7"))