# link : https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    temp_s = [ int(x) for x in s.split(' ') ]
    return '{} {}'.format(min(temp_s), max(temp_s))

print(solution("-1 -2 3 4"))