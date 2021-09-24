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
