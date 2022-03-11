# link : https://www.acmicpc.net/problem/10162

target = int(input())
btn_A, btn_B, btn_C = 300, 60, 10

if target > 0:
    if target % btn_C != 0:
        print(-1)
    else:
        answer = []
        answer.append(target // btn_A)
        target = target % btn_A

        answer.append(target // btn_B)
        target = target % btn_B

        answer.append(target // btn_C)
        
        print('{} {} {}'.format(answer[0], answer[1], answer[2]))