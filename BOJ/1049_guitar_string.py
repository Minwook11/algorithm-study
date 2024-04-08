# link : https://www.acmicpc.net/problem/1049

N, M = list(map(int,input().split()))

N_set, N_single = divmod(N, 6)

answer = 0

set_price_list, single_price_list = [], []
for _ in range(M):
    set_price, single_price = list(map(int,input().split()))

    set_price_list.append(set_price)
    single_price_list.append(single_price)

most_cheap_set, most_cheap_single = min(set_price_list), min(single_price_list)

if most_cheap_set > most_cheap_single * 6:
    answer = N * most_cheap_single
else:
    answer += N_set * most_cheap_set

    if most_cheap_set < most_cheap_single * N_single:
        answer += 1 * most_cheap_set
    else:
        answer += N_single * most_cheap_single

print(answer)