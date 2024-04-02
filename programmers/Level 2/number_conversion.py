# https://school.programmers.co.kr/learn/courses/30/lessons/154538

def solution(x, y, n):
    f_1 = lambda val: 3*val
    f_2 = lambda val: 2*val
    f_3 = lambda val: val+n

    operations = [f_1, f_2, f_3]
    
    overed = set()

    def backtrack(curr, path):
        if curr == y:
            print(f"CHECK : {curr}")
            all_paths.append(len(path))
            return
        if curr > y:
            print(f"BREAK : {curr}")
            overed.add(curr)
            return
        for idx, op in enumerate(operations, start=1):
            print(f"{curr} process formular is f_{idx}")
            cal_curr = op(curr)
            if cal_curr not in overed:
                backtrack(cal_curr, path + [op])
            else:
                print("ALREADY_CHECKED_OVERED")

    print(f"START :{x}")
    all_paths = []
    backtrack(x, [])

    return min(all_paths) if all_paths else -1

print(solution(10, 40, 5))