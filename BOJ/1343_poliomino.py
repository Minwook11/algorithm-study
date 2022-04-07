# link : https://www.acmicpc.net/problem/1343

from re import S


board = input()

if board.count('X') % 2 != 0:
    print(-1)
else:
    stack_space = []
    answer, count = '', 0
    for space in board:
        if space == 'X':
            stack_space.append(space)
        elif space =='.':
            if len(stack_space) % 2 != 0:
                answer = -1
                break
            else:
                answer += '.'
                
        if len(stack_space) == 4:
            answer += 'AAAA'
            stack_space = []
        elif len(stack_space) == 2:
            answer += 'BB'
            stack_space = []
    print(answer)