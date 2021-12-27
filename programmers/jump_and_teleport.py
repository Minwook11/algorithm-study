# link : https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    answer = 0

    while n > 0:
        quote, remain = divmod(n , 2)
        n = quote
        if remain != 0:
            answer += 1

    return answer

print(solution(5000))

# Other programmer's solution -- Most interesting solution
# def solution(n):
#     return bin(n).count('1')