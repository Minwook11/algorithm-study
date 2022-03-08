# link : https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    species = len(list(set(nums)))
    pickable = len(nums) // 2
    
    answer = pickable if species > pickable else species
    return answer

print(solution([1,2,3,4,5,6,7,7,7,7]))