# link : https://www.acmicpc.net/problem/2606

# def dfs(graph, node_index, visited):
#     if len(visited) == len(graph) - 1:
#         return visited
#     if node_index not in visited:
#         visited.append(node_index)
#     visitable = graph[node_index]
#     for next_index in visitable:
#         if next_index not in visited:
#             visited = dfs(graph, next_index, visited)

#     return visited

# def bfs(graph, node_index, visited):
#     if len(visited) == len(graph) - 1:
#         return visited
#     if node_index not in visited:
#         visited.append(node_index)
#     visitable = graph[node_index]
#     next_level = []
#     for next_index in visitable:
#         if next_index not in visited:
#             visited.append(next_index)
#             next_level += graph[next_index]


# N, M, start = list(map(int, input().split()))

# graph = [[] for _ in range(N+1)]

# for _ in range(M):
#     a, b = list(map(int, input().split()))
#     if b not in graph[a]:
#         graph[a].append(b)
#     if a not in graph[b]:
#         graph[b].append(a)

# dfs_visited = dfs(graph, start, [])

# bfs_visited = bfs(graph, start, [])

from collections import deque


def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# dfs
visited = [False] * (N + 1)
dfs(V)
print()

# bfs
visited = [False] * (N + 1)
bfs(V)