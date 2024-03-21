# https://school.programmers.co.kr/learn/courses/30/lessons/12927


def solution(n, works):
    if len(works) > 1:
        index = 0
        while True:
            if index == 50:
                break

            abs_remain_list = sorted(list(set(works)), reverse=True)
            print(abs_remain_list)
            if len(abs_remain_list) > 1:
                largest, larger = abs_remain_list[0], abs_remain_list[1]
                worked = largest - larger
            else:
                largest, larger = abs_remain_list[0], abs_remain_list[0]
                worked = 1

            if largest == 0:
                break
            print(f"works list : {works}, largest : {largest}, larger : {larger}")

            print(f"left hours : {n}, worked : {worked}")
            if n >= worked:
                n -= worked
                works[works.index(largest)] -= worked
            else:
                works[works.index(largest)] -= n
            print(f"left work : {works}")
            if n == 0:
                break

            index += 1
        print(f"{index} 번 반복")
        return sum([i**2 for i in works])
    else:
        remain = works[0] - n if works[0] > n else 0

        return remain ** 2

print(solution(4, [4,3,3]))