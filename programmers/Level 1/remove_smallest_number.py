# link : https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr) > 1:
        arr.remove(sorted(arr)[0])
    else:
        arr = [-1]
    return arr

print(solution([4,3,2,1]))
