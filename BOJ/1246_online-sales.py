# link : https://www.acmicpc.net/problem/1246

egg_count, customer_count = map(int, (input().split()))
customer_offer = []
for _ in range(customer_count):
    customer_offer.append(int(input()))
customer_offer.sort(reverse=True)

answer, price = 0, 0
for i in range(len(customer_offer)):
    temp_count = egg_count if i >= egg_count - 1 else i + 1

    if customer_offer[i] * temp_count > answer: 
        answer = customer_offer[i] * temp_count
        price = customer_offer[i]

print(price, answer)