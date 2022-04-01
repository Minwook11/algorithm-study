# link : https://www.acmicpc.net/problem/16255

from operator import le


match_number = int(input())

test_cases = []

for _ in range(match_number):
    test_cases.append(list(map(int, input().split())))

for test_case in test_cases:
    left_match = test_case[0] - max(test_case[1:])
    score_gap = 2 - abs(test_case[1] - test_case[2])

    # print('{} {}'.format(left_match, score_gap))
    if left_match <= 0:
        print(score_gap)
    else:
        if left_match >= score_gap:
            print(left_match)
        else:
            print(score_gap)