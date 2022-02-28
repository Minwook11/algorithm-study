# link : https://programmers.co.kr/learn/courses/30/lessons/86052/solution_groups?language=python3

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def solution(grid):
    global visited,n,m
    n = len(grid)
    m = len(grid[0])
    answer = []
    visited = [[[False]*4 for _ in range(m)] for _ in range(n)]
    for sx in range(n):
        for sy in range(m):
            for d in range(4):
                if not visited[sx][sy][d]:
                    rst = simul(sx,sy,d,grid)
                    if rst != 0:
                        answer.append(rst)
    answer.sort()
    return answer

def simul(sx,sy,sd,grid):
    global visited
    x,y,d=sx,sy,sd
    cnt = 0
    visited[sx][sy][sd] = True
    while True:
        x = (x + dx[d]) % n
        y = (y + dy[d]) % m
        cnt += 1

        if grid[x][y] == 'R':
            d = (d+1)%4
        elif grid[x][y] == 'L':
            d = (d-1)%4
        if visited[x][y][d]:
            if (x,y,d) == (sx,sy,sd):
                return cnt
            else:
                return 0
        visited[x][y][d] = True

# Other programmer's solution -- Clean code style solution
# delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# def solution(grid):
#     def pathfind(r, c, d):
#         cnt = 0
#         while not visit[r][c][d]:
#             visit[r][c][d] = 1
#             cnt += 1 
#             if grid[r][c] == 'L':
#                 d = (d - 1) % 4
#             elif grid[r][c] == 'R':
#                 d = (d + 1) % 4
#             r = (r + delta[d][0]) % len(grid)
#             c = (c + delta[d][1]) % len(grid[0])
#         return cnt

#     answer = []
#     visit = [[[0] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
#     for r in range(len(grid)):
#         for c in range(len(grid[0])):
#             for d in range(4):
#                 if visit[r][c][d]:
#                     continue
#                 answer.append(pathfind(r, c, d))
#     answer.sort()
#     return answer