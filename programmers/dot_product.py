# link : https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum( [ item1 * item2 for item1, item2 in zip(a, b) ] )

print(solution([1,2,3,4], [-3,-1,0,2]))