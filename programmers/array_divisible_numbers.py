# link : https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []

    for num in sorted(arr):
        if num % divisor == 0:
            answer.append(num)

    return [-1] if len(answer) <= 0 else answer

print(solution([36,2,1,3], 1))

# Other programmer's solution -- Most liked solution
#def solution(arr, divisor):
#    return sorted([n for n in arr if n%divisor == 0]) or [-1]
