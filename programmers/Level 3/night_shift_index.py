# https://school.programmers.co.kr/learn/courses/30/lessons/12927


def solution(n, works):
    if len(works) > 1:
        entire_amount = sum(works)
        after_worked = entire_amount - n
        if after_worked <= 0:
            return 0
        valanced_val, remain = divmod(after_worked, len(works))
        reamin_work_amount = [ valanced_val for _ in range(len(works))]
        if remain > 0:
            for idx in range(len(reamin_work_amount)):
                reamin_work_amount[idx] += 1
                remain -= 1

                if remain == 0:
                    break

        return sum([i ** 2 for i in reamin_work_amount])
    else:
        left_work = works[0] - n if works[0] - n >= 0 else 0
        return left_work ** 2

print(solution(3, [1, 1]))