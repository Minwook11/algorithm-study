# link : https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    answer = 0
    characters = list(numbers)
    temp_data = []

    for i in range(1, len(numbers) + 1):
        temp = list(permutations(characters, i))
        temp_data += [ int(''.join(case)) for case in temp ]

    temp_data = list(set(temp_data))

    for num in temp_data:
        if num < 2:
            continue
        check_flag = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                check_flag = False
                break

        if check_flag:
            answer += 1

    return answer

print(solution('011'))