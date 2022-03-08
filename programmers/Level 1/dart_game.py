# link : https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResults):
    answer = []

    num_stack = []
    for c in dartResults:
        if c.isdigit() == True:
            num_stack.append(c)
        elif c.isalpha() == True:
            score = int(''.join(num_stack))
            num_stack = []
            if c == 'S':
                answer.append(score**1)
            elif c == 'D':
                answer.append(score**2)
            elif c == 'T':
                answer.append(score**3)
        elif c == '*' or c == '#':
            if c == '*':
                if len(answer) > 1:
                    answer[-2] *= 2
                    answer[-1] *= 2
                else:
                    answer[-1] *= 2

            if c == '#':
                answer[-1] *= -1
    
    return sum(answer)

print(solution('10S2D*3T#'))

# Other programmer's solution -- Most interesting solution
# import re
# def solution(dartResult):
#     bonus = {'S' : 1, 'D' : 2, 'T' : 3}
#     option = {'' : 1, '*' : 2, '#' : -1}
#     p = re.compile('(\d+)([SDT])([*#]?)')
#     dart = p.findall(dartResult)
#     for i in range(len(dart)):
#         if dart[i][2] == '*' and i > 0:
#             dart[i-1] *= 2
#         dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

#     answer = sum(dart)
#     return answer