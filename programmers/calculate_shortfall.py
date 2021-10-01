# link : https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    result = 0
    for i in range(1, count + 1):
        result += price * i

    return 0 if (money - result) >=  0 else abs(money - result)

print(solution(3, 20, 4))

# Other programmer's solution -- Most liked solution
#def solution(price, money, count):
#    return max(0,price*(count+1)*count//2-money)
