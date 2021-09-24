# link = https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    keypad = [1,2,3,4,5,6,7,8,9,'*', 0, '#']
    answer = []

    L_h = keypad.index('*')
    R_h = keypad.index('#')

    for number in numbers:
        print('Left : {}, Right : {}'.format(L_h, R_h))

        if number in [1,4,7]:
            answer.append('L')
            L_h = keypad.index(number)
        elif number in [3,6,9]:
            answer.append('R')
            R_h = keypad.index(number)
        else:
            number_index = keypad.index(number)
            temp_left = (abs(number_index - L_h) // 3) + (abs(number_index - L_h) % 3)
            temp_right = (abs(number_index - R_h) // 3) + (abs(number_index - R_h) % 3)

            print('target_index = {}, letf_index = {}, right_index = {}'.format(number_index, temp_left, temp_right))

            if temp_right == temp_left:
                if hand == 'left':
                    answer.append('L')
                    L_h = keypad.index(number)
                elif hand == 'right':
                    answer.append('R')
                    R_h = keypad.index(number)

            else:
                if temp_left > temp_right:
                    answer.append('R')
                    R_h = keypad.index(number)
                elif temp_left < temp_right:
                    answer.append('L')
                    L_h = keypad.index(number)

    return ''.join(answer)

number_list = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

print(solution(number_list, hand))

# Other programmer's solution -- Most liked solution
#def solution(numbers, hand):
#    answer = ''
#    key_dict = {1:(0,0),2:(0,1),3:(0,2),
#                4:(1,0),5:(1,1),6:(1,2),
#                7:(2,0),8:(2,1),9:(2,2),
#                '*':(3,0),0:(3,1),'#':(3,2)}
#
#    left = [1,4,7]
#    right = [3,6,9]
#    lhand = '*'
#    rhand = '#'
#    for i in numbers:
#        if i in left:
#            answer += 'L'
#            lhand = i
#        elif i in right:
#            answer += 'R'
#            rhand = i
#        else:
#            curPos = key_dict[i]
#            lPos = key_dict[lhand]
#            rPos = key_dict[rhand]
#            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
#            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
#
#            if ldist < rdist:
#                answer += 'L'
#                lhand = i
#            elif ldist > rdist:
#                answer += 'R'
#                rhand = i
#            else:
#                if hand == 'left':
#                    answer += 'L'
#                    lhand = i
#                else:
#                    answer += 'R'
#                    rhand = i
#
#    return answer
