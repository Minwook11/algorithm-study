# link : https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0

    available_position = set()
    for route in sorted(routes, key=lambda x:x[0]):
        # print(route)
        input_list = [i for i in range(route[0], route[1] + 1)]
        # print(available_position)
        check_res = available_position.intersection(set(input_list))
        # print(check_res)
        if check_res:
            available_position = check_res
        else:
            answer += 1
            available_position = set(input_list)

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))