# link : https://programmers.co.kr/learn/courses/30/lessons/77884

def cal_factors(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        answer = answer + num if cal_factors(num) % 2 == 0 else answer - num
    return answer

print(solution(13, 17))

# Other programmer's solution -- Most liked solution
#def solution(left, right):
#    answer = 0
#    for i in range(left,right+1):
#        if int(i**0.5)==i**0.5:
#            answer -= i
#        else:
#            answer += i
#    return answer
