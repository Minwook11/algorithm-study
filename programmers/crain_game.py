# link : https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    res_queue = []
    score = 0
    for pos in moves:
        for i in range(len(board[0])):
            if board[i][pos - 1] != 0:
                res_queue.append(board[i][pos - 1])
                board[i][pos - 1] = 0
                break

        if len(res_queue) >= 2:
            if res_queue[-1] == res_queue[-2]:
                score += 2
                res_queue = res_queue[:-2] if len(res_queue) > 2 else [0]
    return score

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
