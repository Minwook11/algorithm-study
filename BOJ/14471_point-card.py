# link : https://www.acmicpc.net/problem/14471

places, cards = map(int, input().split())

target = cards - 1
fail_card = []
for _ in range(cards):
    check, fail = map(int, input().split())

    if check >= places:
        target -= 1
    else:
        fail_card.append(check)

fail_card.sort(reverse=True)

answer = 0
if target <= 0:
    print(answer)
else:
    for i in range(target):

        answer += places - fail_card[i]
        print('a : {}'.format(answer))

    print(answer)