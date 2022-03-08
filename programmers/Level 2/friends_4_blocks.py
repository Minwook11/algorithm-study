# link : https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m ,n, board):
    for i in range(len(board)):
        board[i] = list(board[i])
    print(board)
    answer = 0

    x_pos, y_pos = 0, 0
    removed = []

    flag = 0

    while True:
        # print('y : {}, x : {}'.format(y_pos, x_pos))
        if flag > 10000:
            break

        if x_pos == n - 1:
            x_pos = 0
            y_pos += 1
            continue
        
        if y_pos == m - 1:
            if removed:
                for pos in removed:
                    x, y = pos[1], pos[0]
                    board[y][x], board[y + 1][x], board[y][x + 1], board[y + 1][x + 1] = 1, 1, 1, 1
                temp_board = []
                for x in range(n):
                    temp_line = []
                    for y in range(m):
                        temp_line.append(board[y][x])

                    count = temp_line.count(1)
                    answer += count
                    if count == 0:
                        temp_board.append(temp_line[::-1])
                        continue

                    temp_line = temp_line[::-1]
                    for i in range(count):
                        temp_line.remove(1)
                        temp_line.append('0')
                    temp_board.append(temp_line)

                process_board = []
                for x in range(m):
                    temp_line = []
                    for y in reversed(range(n)):
                        temp_line.append(temp_board[y][x])
                    process_board.append(temp_line)

                board = process_board
                x_pos, y_pos = 0, 0
                removed = []
                continue

            else:
                break

        first = board[y_pos][x_pos]
        second = board[y_pos + 1][x_pos]
        third = board[y_pos][x_pos + 1]
        fourth = board[y_pos + 1][x_pos + 1]

        if first.isdigit():
            x_pos += 1
            flag += 1
            continue

        if first == second == third == fourth:
            removed.append([y_pos, x_pos])

        x_pos += 1
        flag += 1

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

# Other programmer's solution -- Most simpliest solution
# def pop_num(b, m, n):
#     pop_set = set()
#     # search
#     for i in range(1, n):
#         for j in range(1, m):
#             if b[i][j] == b[i-1][j-1] == b[i-1][j] == b[i][j-1] != '_':
#                 pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
#     # set_board
#     for i, j in pop_set:
#         b[i][j] = 0        
#     for i, row in enumerate(b):
#         empty = ['_'] * row.count(0)
#         b[i] = empty + [block for block in row if block != 0]
#     return len(pop_set)
     
# def solution(m, n, board):
#     count = 0
#     b = list(map(list,zip(*board)))
#     while True:
#         pop = pop_num(b, m, n)
#         if pop == 0: return count
#         count += pop