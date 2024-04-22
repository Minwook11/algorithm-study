# link : https://www.acmicpc.net/problem/14248

def dfs(pos, jump_scale, visited):
    scale = jump_scale[pos]
    temp_pos = []
    if pos - scale >= 0:
        temp_pos.append(pos-scale)
    if pos + scale <= len(jump_scale) - 1:
        temp_pos.append(pos+scale)

    for next_pos in temp_pos:
        if next_pos not in visited:
            visited.append(next_pos)
        dfs(next_pos, JUMP_SCALE, visited)

N = int(input()) - 1
JUMP_SCALE = list(map(int, input().split()))
start = int(input()) - 1

visited = []

dfs(start, JUMP_SCALE, visited)

print(len(visited) + 1)