# link : https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    prime = [2]
    if n == 2: return len(prime)

    temp_num_list = [ x for x in range(3, n + 1) if x % 2 != 0 ]
    for i in temp_num_list:
        pass_chk = 0
        for prime_num in prime:
            if i % prime_num == 0:
                pass_chk = 1
                break

        if pass_chk == 0:
            prime.append(i)

    return len(prime)

print(solution(10))

# Other programmer's solution -- Efficiency chech passed solution Reference
# def solution(n):
#     num=set(range(2,n+1))

#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)