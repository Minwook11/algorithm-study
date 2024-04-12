# link : https://www.acmicpc.net/problem/2847

level_count = int(input())

answer = 0
score_list = []
for i in range(level_count):
    score_list.insert(0, int(input()))
print(score_list)
for i in range(1, level_count):
    print(score_list[i-1], score_list[i])
    if score_list[i-1] <= score_list[i]:
        fix_score = abs(score_list[i-1] - score_list[i] - 1)
        print(fix_score)
        score_list[i] -= fix_score
        answer += fix_score

print(answer)