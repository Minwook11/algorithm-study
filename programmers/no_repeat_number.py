# link : https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = [arr[0]]

    for i in arr:
        if i != answer[-1]:
            answer.append(i)
            check = i

    return answer

print(solution([1,1,3,3,0,1,1]))
