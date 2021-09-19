# link : https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3

def solution(lottos, win_nums):
    zero_count = lottos.count(0)

    if zero_count == 6:
        return [1, 6]
    elif zero_count < 6:
        win_res = 0
        for i in lottos:
            for j in win_nums:
                if i == j: win_res += 1

        if win_res == 6:
            return [1, 1]

        else:
            return [ (7 - (win_res + zero_count) if win_res + zero_count > 0 else 6), (7 - win_res if win_res > 0 else 6) ]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))

# Other programmer's solution
#def solution(lottos, win_nums):
#
#    rank=[6,6,5,4,3,2,1]
#
#    cnt_0 = lottos.count(0)
#    ans = 0
#    for x in win_nums:
#        if x in lottos:
#            ans += 1
#    return rank[cnt_0 + ans],rank[ans]
