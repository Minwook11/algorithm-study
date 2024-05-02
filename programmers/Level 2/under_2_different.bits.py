# link : https://school.programmers.co.kr/learn/courses/30/lessons/77885?language=python3

def solution(numbers):
    answer = []
    for number in numbers:
        current_bin = bin(number)[2:]
        
        i = 1
        while True:
            next_number = number + i
            next_bin = bin(next_number)[2:]
            if len(next_bin) != len(current_bin):
                for _ in range(len(next_bin) - len(current_bin)):
                    current_bin = "0" + current_bin

            diff_count = 0
            for c, n in zip(current_bin[::-1], next_bin[::-1]):
                if c != n:
                    diff_count += 1
                
                if diff_count > 2:
                    break
            if diff_count < 3:
                answer.append(next_number)
                break

            i += 1

    return answer

print(solution([312, 11, 7, 5, 3, 27, 75, 10, 12, 26, 324, 5236]))