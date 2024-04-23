# link : https://www.acmicpc.net/problem/13565

# graph = []
# check_flag = False

# def dfs(coord_y, coord_x, restrict, check_flag):
#     print(f"current pos -- Y:{coord_y}, X:{coord_x}")
#     next_points = []
#     for coord in [[coord_y - 1, coord_x], [coord_y, coord_x-1], [coord_y, coord_x+1]]:
#         if coord[0] >= 0 and coord[1] >= 0 and coord[1] < restrict:
#             if graph[coord[0]][coord[1]] == "0":
#                 next_points.append(coord)

#     print(next_points)
#     for coord_y, coord_x in next_points:
#         if coord_y == 0:
#             check_flag = True
#             break
#         else:
#             check_flag = dfs(coord_y, coord_x, restrict, check_flag)

#     return check_flag


# Y, X = list(map(int, input().split()))

# for _ in range(Y):
#     graph.append(list(input()))
# print(graph[0][0])
# start_points = []
# for i in range(X):
#     if graph[Y-1][i] == "0":
#         start_points.append([Y-1, i])
# print(start_points)
# for coord_y, coord_x in start_points:
#     if not check_flag:
#         check_flag = dfs(coord_y, coord_x, X, check_flag)
# print(check_flag)

# answer = "YES" if check_flag else "NO"
# print(answer)

import sys
sys.setrecursionlimit(3000000)

def dfs(y, x):
    graph[y][x] = 2
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == 0:
            dfs(Y, X)
            
M, N = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(M)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for j in range(N):
    if graph[0][j] == 0:
        dfs(0, j)
print("YES" if 2 in graph[-1] else "NO")