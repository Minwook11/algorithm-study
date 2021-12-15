# link : https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse = True)

    for i, j in zip(A, B):
        answer += int(i * j)

    return answer

print(solution([1, 2], [3, 4]))