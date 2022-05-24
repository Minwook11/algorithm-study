# link : https://www.acmicpc.net/problem/11508

product_count = int(input())
price_list = [ int(input()) for _ in range(product_count) ]

price_list.sort(reverse=True)
answer = 0

for i in range(len(price_list)):
    if i % 3 != 2:
        answer += price_list[i]

print(answer)