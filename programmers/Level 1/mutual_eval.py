# link : https://programmers.co.kr/learn/courses/30/lessons/83201

def solution(scores):
    avg_scores = []
    for index in range(len(scores[0])):
        scored_list = [ scores[i][index] for i in range(len(scores[0])) ]

        if scored_list[index] == max(scored_list) and scored_list.count(max(scored_list)) == 1:
            temp_score = sorted(scored_list)
            avg_scores.append(sum(temp_score[:-1]) / (len(temp_score[:-1]) * 1.0))
        elif scored_list[index] == min(scored_list) and scored_list.count(min(scored_list)) == 1:
            temp_score = sorted(scored_list)
            avg_scores.append(sum(temp_score[1:]) / (len(temp_score[1:]) * 1.0))
        else:
            avg_scores.append(sum(scored_list) / (len(scored_list) * 1.0))

    grade_list = []
    for i in avg_scores:
        if i >= 90:
            grade_list.append('A')
            continue
        elif i >= 80:
            grade_list.append('B')
            continue
        elif i >= 70:
            grade_list.append('C')
            continue
        elif i >= 50:
            grade_list.append('D')
            continue
        else:
            grade_list.append('F')
            continue

    return ''.join(grade_list)

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))

# Other programmer's solution -- Most liked and imporessive solution
#solution = lambda scores: "".join(map(lambda m: "FDDCBAA"[max(int(sum(m) / len(m) / 10) - 4, 0)], map(lambda m: (m[0], *m[1]) if min(m[1]) <= m[0] <= max(m[1]) else m[1], ((s[i], s[:i] + s[i+1:]) for i, s in enumerate(zip(*scores))))))
