# link : https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        answer = answer + num if sign else answer - num

    return answer

abs_nums = [4, 7, 12]
num_signs = [True, False, True]

print(solution(abs_nums, num_signs))

# Other programmer's solution -- Most liked solution
#def solution(absolutes, signs):
#    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
