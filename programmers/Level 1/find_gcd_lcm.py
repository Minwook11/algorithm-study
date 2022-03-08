# link : https://programmers.co.kr/learn/courses/30/lessons/12940

def gcd(n1, n2):
    if n1 < n2:
        (n1, n2) = (n2, n1)

    while n2 != 0:
        (n1, n2) = (n2, n1 % n2)

    return n1

def solution(n, m):
    return [gcd(n, m), int((n * m) / gcd(n,m))]

print(solution(4, 6))