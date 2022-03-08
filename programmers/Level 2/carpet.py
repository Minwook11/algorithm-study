# link : https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, red):
    all_squares = brown + red
    answer = []

    divisors = [ x for x in range(3, all_squares + 1) if all_squares % x == 0 and all_squares // x >= 3 ]

    for x_len in divisors[::-1]:
        y_len = all_squares // x_len

        if red == (x_len - 2) * (y_len - 2):
            answer.append(x_len)
            answer.append(y_len)
            break

    answer.sort(reverse = True)

    return answer

print(solution(8, 1))