# link : https://programmers.co.kr/learn/courses/30/lessons/77485

# def solution(rows, columns, queries):
#     temp_matrix = []
#     for i in range(rows):
#         temp_matrix.append([])
#         for j in range((columns * i) + 1, (columns * i) + columns + 1):
#             temp_matrix[i].append(j)

#     for i in temp_matrix:
#         print(i)

#     for query in queries:
#         x_len = query[2] - query[0] + 1
#         y_len = query[3] - query[1] + 1
#         rotate_count = (x_len * y_len) - ((x_len - 2) * (y_len - 2))
#         current = [query[0] - 1, query[1] - 1]
#         turn = [query[2] - 1, query[3] - 1]

#         print('turn index x : {}, y : {}'.format(turn[0], turn[1]))

#         temp_next_num = 0
#         phase_counter = 0
#         for rotate in range(rotate_count + 1):
#             current_num = temp_matrix[current[0]][current[1]]
#             print('current index check - current x : {}, turn x : {}, current y : {}, turn y : {}'.format(current[0], turn[0], current[1], turn[1]))
#             print('current num : {}'.format(current_num))
#             if phase_counter == 0:
#                 current[1] = current[1] + 1
#             elif phase_counter == 1:
#                 current[0] = current[0] + 1
#             elif phase_counter == 2:
#                 current[1] = current[1] - 1
#             elif phase_counter == 3:
#                 current[0] = current[0] - 1
#             temp_next_num = temp_matrix[current[0]][current[1]]
#             print('next temp num : {}'.format(temp_next_num))
#             temp_matrix[current[0]][current[1]] = current_num

#             if phase_counter == 0 and current[1] == turn[1]:
#                 print('phase 1 shift')
#                 phase_counter = 1
#             elif phase_counter == 1 and current[0] == turn[0] and current[1] == turn[1]:
#                 print('phase 2 shift')
#                 phase_counter = 2
#             elif phase_counter == 2 and current[1] == query[1]:
#                 print('phase 3 shift')
#                 phase_counter = 3
#             elif phase_counter == 3 and current[0] == query[0] and current[1] == query[1]:
#                 print('phase 4 shift')
#                 phase_counter = 4

#     return 1

def solution(rows, columns, queries):
    answer = []
    table = []
    for r in range(rows):
        table.append([a for a in range(r*columns+1, (r+1)*columns+1)])
    
    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1]+1] = tmp
        
        answer.append(small)
    
    return answer