# link : https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    answer = 0

    memorize = [ 0 for _ in range(n) ]

    for i in range(n):
        if i == 0:
            memorize[i] = 1
        elif i == 1:
            memorize[i] = 2
        else:
            memorize[i] += (memorize[i - 1] + memorize[i - 2]) % 1000000007

    answer = memorize[-1]

    return answer

print(solution(5))

# Other programmer's solution -- Most Simpliest solution
# def solution(n):
#     a, b = 1, 1
#     for i in range(1, n):
#         a, b = b, (a + b) % 1000000007
#     return b