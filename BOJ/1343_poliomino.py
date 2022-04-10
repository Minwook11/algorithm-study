# link : https://www.acmicpc.net/problem/1343

from re import S


board = input()

if board.count('X') % 2 != 0:
    print(-1)
else:
    board = board.replace('XXXX', 'AAAA')
    board = board.replace('XX', 'BB')
    print(board)
    
# board = input()

# board = board.replace('XXXX', 'AAAA')
# board = board.replace('XX', 'BB')

# if 'X' in board:
#     print(-1)
# else:
#     print(board)