# link : https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    visited = [[False] * n for _ in range(n)]
    
    def dfs(i, j):
        visited[i][j], visited[j][i] = True, True

        for k in range(n):
            if not visited[j][k] and computers[j][k] == 1:
                print('IN DFS -- j : {}, k : {}'.format(j, k))
                dfs(j, k)
            
    count = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and computers[i][j] == 1:
                print('IN SOLUTION -- i : {}, j : {}'.format(i, j))
                dfs(i, j)
                count += 1
    
    return count

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# Other programmer's solution -- Most interesting solution
# def solution(n, computers):
#     temp = []
#     for i in range(n):
#         temp.append(i)
#     for i in range(n):
#         for j in range(n):
#             if computers[i][j]:
#                 for k in range(n):
#                     if temp[k] == temp[i]:
#                         temp[k] = temp[j]
#     return len(set(temp))