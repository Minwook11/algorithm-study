# link : https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        temp = budget - d[i]
        if temp < 0:
            break
        elif temp == 0:
            answer += 1
            break
        else:
            answer += 1
        budget = temp
    return answer

print(solution([3, 1, 5, 1, 2], 10))

# Other programmer's solution -- Solution similar to mine
#def solution(d, budget):
#    d.sort()
#    cnt = 0
#    for i in d :
#        budget -= i
#        if budget < 0 :
#               break
#        cnt += 1
#    answer = cnt
#    return answer
