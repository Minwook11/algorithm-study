# link : https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    answer = 1
    while True:
        if a // 2 + a % 2 == b // 2 + b % 2: break
        
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        
        answer += 1
        
    return answer

print(solution(8, 3, 5))

# Other programmer's solution -- Most Simpliest solution
# def solution(n,a,b):
#     return ((a-1)^(b-1)).bit_length()