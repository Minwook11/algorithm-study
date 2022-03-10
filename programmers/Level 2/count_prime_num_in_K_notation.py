# link : https://programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    word = ''

    while n:
        word += str(n%k)
        n = n//k

    word = word[::-1]

    removed_zero = word.split('0')
    temp_list = [ i for i in removed_zero if len(i) > 0 ]

    li=list(map(int, temp_list))


    count = 0
    for i in li:
        prime_num = True
        if i < 2:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime_num = False
                break
        if prime_num:
            count += 1

    return count

print(solution(437674, 3))