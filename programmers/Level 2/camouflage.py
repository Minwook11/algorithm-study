# link : https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    closet = {}
    answer = 1
    
    for cloth in clothes:
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]
    
    for value in closet.values():
        answer *= len(value) + 1
    
    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))