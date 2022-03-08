# link : https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = ''
    temp_stack = ''

    for c in s:
        if c.isdigit():
            answer += c
        else:
            temp_stack += c

            if temp_stack == 'zero':
                answer += '0'
                temp_stack = ''
                continue
            elif temp_stack == 'one':
                answer += '1'
                temp_stack = ''
                continue
            elif temp_stack == 'two':
                answer += '2'
                temp_stack = ''
                continue
            elif temp_stack == 'three':
                answer += '3'
                temp_stack = ''
                continue
            elif temp_stack == 'four':
                answer += '4'
                temp_stack = ''
                continue
            elif temp_stack == 'five':
                answer += '5'
                temp_stack = ''
                continue
            elif temp_stack == 'six':
                answer += '6'
                temp_stack = ''
                continue
            elif temp_stack == 'seven':
                answer += '7'
                temp_stack = ''
                continue
            elif temp_stack == 'eight':
                answer += '8'
                temp_stack = ''
                continue
            elif temp_stack == 'nine':
                answer += '9'
                temp_stack = ''
                continue

    return int(answer)

print(solution("one4seveneight"))

# Other programmer's solution -- Most simpliest solution
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)