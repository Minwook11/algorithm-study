# link : https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    if s[0] == ')' or s[-1] == '(' : return False
    if len(s) % 2 != 0 : return False

    check_result = 0
    for c in s:
        if check_result == 0 and c == ')':
            check_result = -1
            break

        if c == '(' : check_result += 1
        else : check_result -= 1


    return True if check_result == 0 else False

print(solution('()())()'))