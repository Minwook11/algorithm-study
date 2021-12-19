# link : https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    divisor = 2
    while True:
        remain = n % divisor

        if remain != 1:
            divisor += 1
        elif remain == 1:
            break

    return divisor
        
print(solution(12))