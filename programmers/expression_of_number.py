# link : https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    if n == 1 or n == 2: return 1

    answer = 0

    for start in range(n + 1, 0, -1):
        if start == n:
            answer += 1
            continue

        if n - start < start - 1: 
            continue
        else:
            temp_data = 0
            for i in range(start, 0, -1):
                temp_data += i
                if temp_data == n:
                    answer += 1
                    break
                elif temp_data > n:
                    break
    
    return answer

print(solution(15))