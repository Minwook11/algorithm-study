# link : https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    answer = 0
    route = [0]*(n+1)
    edge.sort()
    queue = deque() 
    graph = [[] for i in range(n+1)]
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    queue.append(1)
    route[1] = 1
    print(queue)
    while queue:
        now = queue.popleft()
        for g in graph[now]:
            if route[g]==0:
                queue.append(g)
                route[g] = route[now]+1
        
    max_edge= max(route)
    for r in route:
        if r == max_edge:
            answer+=1     
            
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

# Other programmer's solution --  BFS Solution
# from collections import deque

# def bfs(v, visited, adj):
#     count = 0
#     q = deque([[v, count]])
#     while q:
#         value = q.popleft()
#         v = value[0]
#         count = value[1]
#         if visited[v] == -1:
#             visited[v] = count
#             count += 1
#             for e in adj[v]:
#                 q.append([e, count])

# def solution(n, edge):
#     answer = 0
#     visited = [-1] * (n + 1)
#     adj = [[] for _ in range(n + 1)]
#     for e in edge:
#         x = e[0]
#         y = e[1]
#         adj[x].append(y)
#         adj[y].append(x)
#     bfs(1, visited, adj)
#     for value in visited:
#         if value == max(visited):
#             answer += 1
#     return answer