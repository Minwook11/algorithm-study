# link : https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    count = 0
    i = 0
    for i in range(len(s)):
        stack = []
        for j in s:
            if not stack:
                stack.append(j)
                continue
            if stack[-1] == '[' and j == ']':
                stack.pop()
            elif stack[-1] == '{' and j == '}':
                stack.pop()
            elif stack[-1] == '(' and j == ')':
                stack.pop()
            else:
                stack.append(j)
        s = s[1:] + s[0]
        if not stack:
            count += 1
    return count

print(solution("[](){}"))


# Other programmer's solution
# from collections import deque

# def check(s):
#     stack = []
#     for c in s:
#         if c == '(' or c == '{' or c == '[':
#             stack.append(c)
#         else:
#             if not stack:
#                 return False
#             x = stack.pop()
#             if c == ')' and x != '(':
#                 return False
#             elif c == ')' and x != '(':
#                 return False
#             elif c == '}' and x != '{':
#                 return False
#     return len(stack) == 0

# def solution(s):
#     s = deque(s)
#     answer = 0
#     for x in range(len(s)):
#         s.rotate(-1)
#         if check(s):
#             answer += 1
#     return answer