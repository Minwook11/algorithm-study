# link : https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    return 45 - sum(numbers)

print(solution([1,2,3,4,5,6,7,8,0]))

# Other programmer's solution
#solution = lambda x: sum(range(10)) - sum(x)
