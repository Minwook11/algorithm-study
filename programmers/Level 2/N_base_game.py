# link : https://school.programmers.co.kr/learn/courses/30/lessons/17687

def convert(number, n):
    if number == 0:
        return '0'
    NUMBERS = "0123456789ABCDEF"
    res = ""
    while number > 0:
        number, mod = divmod(number, n)
        res += NUMBERS[mod]
    return res[::-1]

def solution(n, t, m, p):
    answer = ''
    game = ''
    cur = p - 1
    for num in range(t * m):
        game += convert(num, n)
    while 1:
        if len(answer) == t:
            break
        answer += game[cur]
        cur += m
    return answer

print(solution(2, 4, 2, 1))