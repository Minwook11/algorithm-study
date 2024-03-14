# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    score_board = {name : yearning for name, yearning in zip(name, yearning)}
    
    answer = []

    for target in photo:
        score = 0
        for person in target:
            score += score_board.get(person, 0)
        answer.append(score)
    return answer

print(solution(
        ["may", "kein", "kain", "radi"], 
        [5, 10, 1, 3], 
        [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
    )
)