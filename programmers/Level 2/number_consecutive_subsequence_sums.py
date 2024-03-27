# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    answer = elements + [sum(elements)]
    elements_len = len(elements)

    for length in range(1,elements_len):
        total = sum(elements[:length])
        start, end = 0, length
        for _ in range(elements_len):
            total += elements[end] - elements[start]
            start, end = start+1, (end+1)%elements_len
            answer.append(total)
    
    return len(set(answer))

print(solution([7,9,1,1,4]))