# link : https://www.acmicpc.net/problem/15720

from dis import dis


burger_num, side_num, drink_num = map(int, input().split())

burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))

no_discount = sum(burgers + sides + drinks)
print(no_discount)

set_available = min(burger_num, side_num, drink_num)

burgers.sort()
sides.sort()
drinks.sort()

discount = 0
for _ in range(set_available):
    temp = int((burgers.pop() + sides.pop() + drinks.pop()) * 0.9)
    discount += temp

discount += sum(burgers + sides + drinks)
print(discount)