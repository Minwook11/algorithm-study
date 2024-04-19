# link : https://www.acmicpc.net/problem/2606

def dfs(graph, node_index, infected):
    infected[node_index] = 1
    for i in graph[node_index]:
        if infected[i] == 0:
            dfs(graph, i, infected)


N = int(input())
P = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(P):
    input_pair = list(map(int, input().split()))
    graph[input_pair[0]].append(input_pair[1])
    graph[input_pair[1]].append(input_pair[0])

infected = [0] * (N + 1)

dfs(graph, 1, infected)

print(sum(infected) - 1)