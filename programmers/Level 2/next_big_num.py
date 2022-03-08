# link : https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    count_0 = bin(n).count('1')
    for i in range(n + 1, int('1' + bin(n)[2:], 2)):
        if bin(i).count('1') == count_0:
            return i

print(solution(15))