# link : https://www.acmicpc.net/problem/24444

from collections import deque

M, N, start = list(map(int, input().split()))

graph = [[] for _ in range(M + 1)]
answer = [0 for _ in range(M + 1)]

for _ in range(N):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(M + 1):
    graph[i].sort()

count = 0

next_node_q = deque()

for index in graph[start]:
    # print(index)
    answer[start] = 1
    next_node_q.append(index)

count += 1 

while next_node_q:
    # print(next_node_q)
    next_node = next_node_q.popleft()
    count += 1
    if answer[next_node] == 0:
        answer[next_node] = count

    for index in graph[next_node]:
        if answer[index] == 0:
            next_node_q.append(index)

for i in answer[1:]:
    print(i)