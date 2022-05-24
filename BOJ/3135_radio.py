# link : https://www.acmicpc.net/problem/3135

current, goal = map(int, input().split())
bookmark_cnt = int(input())

bookmarks = [ int(input()) for _ in range(bookmark_cnt) ]

# basic_move = abs(current - goal) if abs(current - goal) <= 500 else 1000 - abs(current - goal)
basic_move = abs(current - goal)
print("Basic : {}".format(basic_move))
for bookmark in bookmarks:
    # movement = abs(bookmark - goal) + 1 if abs(bookmark - goal) <= 500 else 1000 - abs(bookmark - goal) + 1
    movement = abs(bookmark - goal) + 1
    print("Bookmark move : {}".format(movement))
    if basic_move > movement:
        basic_move = movement

print(basic_move)