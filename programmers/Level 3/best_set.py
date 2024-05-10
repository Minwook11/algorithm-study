# link : https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = [-1]

    if n == s:
        return [1] * n

    val, remain = divmod(s, n)
    if val == 0:
        return answer
    else:
        if remain > 0:
            small_cnt = n - remain
            large_cnt = remain

            answer = [val] * small_cnt + [val + 1] * large_cnt
        else:
            answer = [val] * n

    return answer

print(solution(2, 8))