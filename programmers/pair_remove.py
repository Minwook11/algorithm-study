# link : https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    if len(s) < 2:
        return 0
    
    temp_stack = [s[0]]

    for i in range(1, len(s)):
        if len(temp_stack) > 0 and temp_stack[-1] == s[i]:
            temp_stack.pop()
        else:
            temp_stack.append(s[i])

    if len(temp_stack) > 0:
        return 0
    else:
        return 1

print(solution('baabaa'))