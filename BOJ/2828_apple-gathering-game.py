# link : https://www.acmicpc.net/problem/2828

line, basket_size = map(int, input().split())
apple_count = int(input())
basket = [ i + 1 for i in range(basket_size)]

moved = 0
for _ in range(apple_count):
    drop_pos = int(input())
    print(basket)
    if drop_pos not in basket:
        if drop_pos < min(basket):
            moved_len = min(basket) - drop_pos
            basket = [ i - moved_len for i in basket ]
            moved += moved_len
        elif drop_pos > max(basket):
            moved_len = drop_pos - max(basket)
            basket = [ i + moved_len for i in basket ]
            moved += moved_len
    print(basket)

print(moved)