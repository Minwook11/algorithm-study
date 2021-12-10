# link : https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(n):
    if n == 1: return 0
    
    answer = -1
    for count in range(1, 500 + 1):
        print('Count : {}'.format(count))
        n = n // 2 if n % 2 == 0 else int(n * 3) + 1

        if n == 1:
            answer = count
            break

    return answer

print(solution(626331))