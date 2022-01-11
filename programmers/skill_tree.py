# link : https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_tree):
    answer = 0

    for tree in skill_tree:
        temp_stack = []
        for c in tree:
            if c in skill:
                temp_stack.append(c)

        if len(temp_stack) > 0:
            if skill[:len(temp_stack)] == ''.join(temp_stack):
                answer += 1
        else:
            answer += 1

    return answer

print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]))