# link : https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    if n <= 3:
        return '124'[n - 1]
    else:
        s, r = divmod(n - 1, 3)
        return solution(s) + '124'[r]

# Other programmer's solution -- Most interesting solution
#solution = lambda n: (solution(i) if (i := (n - 1) // 3) else "") + "124"[(n - 1) % 3]
