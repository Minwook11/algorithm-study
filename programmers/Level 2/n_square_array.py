# link : https://programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
    for i in range(left,right + 1):
        a, b = i//n, i%n
        if a < b:
            a,b = b,a
        answer.append(a + 1)
    
    return answer

print(solution(4, 7, 14))

# Other programmer's solution -- Most simpliest solution
# def solution(n, left, right):
    # result = lambda n, left, right: list((max(i // n, i % n) + 1 for i in range(left, right + 1)))
    # return result(n, left, right)