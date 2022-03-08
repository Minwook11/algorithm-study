# link : https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = [0,1]
    for i in range(2,n+1):
        answer.append((answer[i-1] + answer[i-2]) % 1234567)
    
    return answer[-1]	

print(solution(5))

# Other programmer's solution
# def solution(n):
#     f_list = [0,1]
#     for i in range(2,n+1):
#         f_list.append((f_list[i-2]%1234567+f_list[i-1]%1234567)%1234567)
#     return f_list[-1]