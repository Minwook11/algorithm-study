# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    lane_1, lane_2 = [], []
    for idx, item in enumerate(food[1:], start=1):
        food_set_qty = item // 2
        for _ in range(food_set_qty):
            lane_1.append(str(idx))
            lane_2.insert(0, str(idx))

    return "".join(lane_1 + ["0"] + lane_2)

print(solution([1,7,1,2]))

# def solution(food):
#     first = ''.join(str(foodNumber) * (quantity // 2) for foodNumber, quantity in enumerate(food))
#     second = first[::-1]
#     answer = first + '0' + second

#     return answer