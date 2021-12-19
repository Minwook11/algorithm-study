# link : https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    pick_1 = [1,2,3,4,5]
    pick_2 = [2,1,2,3,2,4,2,5]
    pick_3 = [3,3,1,1,2,2,4,4,5,5]

    tester_1 = pick_1[:len(answers)] if len(answers) <= 5 else (pick_1 * (1 + (len(answers) // 5)))[: -(5 * (1 + (len(answers) // 5)) - len(answers))]
    tester_2 = pick_2[:len(answers)] if len(answers) <= 8 else (pick_2 * (1 + (len(answers) // 8)))[: -(8 * (1 + (len(answers) // 8)) - len(answers))]
    tester_3 = pick_3[:len(answers)] if len(answers) <= 10 else (pick_3 * (1 + (len(answers) // 10)))[: -(10 * (1 + (len(answers) // 10)) - len(answers))]

    scoreboard = {
        1 : 0,
        2 : 0,
        3 : 0
    }

    for i in range(len(answers)):
        if answers[i] == tester_1[i]:
            scoreboard[1] += 1
        if answers[i] == tester_2[i]:
            scoreboard[2] += 1
        if answers[i] == tester_3[i]:
            scoreboard[3] += 1
    
    top_scored = max([ x for x in scoreboard.values() ])
    answer = [ x for x, y in scoreboard.items() if y == top_scored ]

    return sorted(answer)

print(solution([1,2,3,4,5,1,2,3,4,5,1]))

# Other programmer's solution -- Most interesting solution
# from itertools import cycle

# def solution(answers):
#     giveups = [
#         cycle([1,2,3,4,5]),
#         cycle([2,1,2,3,2,4,2,5]),
#         cycle([3,3,1,1,2,2,4,4,5,5]),
#     ]
#     scores = [0, 0, 0]
#     for num in answers:
#         for i in range(3):
#             if next(giveups[i]) == num:
#                 scores[i] += 1
#     highest = max(scores)

#     return [i + 1 for i, v in enumerate(scores) if v == highest]