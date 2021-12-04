# link : https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    trucks_queue = { truck : 0 for truck in truck_weights }

    passed_truck = []
    answer = 0
    bridge = []
    current = 0
    temp_count = 0
    while passed_truck != truck_weights:
        print(current)
        answer += 1
        if len(bridge) == 0:
            bridge.append(truck_weights[current])
            current += 1
        else:
            if len(bridge) <= bridge_length and sum(bridge) + truck_weights[current] <= weight:
                bridge.append(truck_weights[current])
                current += 1
        
        for truck in bridge:
            print(trucks_queue[truck])
            trucks_queue[truck] += 1
            if trucks_queue[truck] == bridge_length:
                passed_truck.append(truck)
                bridge = bridge[1:]

        print('passed : {}'.format(passed_truck))
        print('truck_weights : {}'.format(truck_weights))
        temp_count += 1

        if temp_count == 10:
            break
    return answer

print(solution(2, 10, [7, 4, 5, 6]))

# Other programmer's solution
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     trucks_on_bridge = [0] * bridge_length
#     while len(trucks_on_bridge):
#         answer += 1
#         trucks_on_bridge.pop(0)
#         if truck_weights:
#             if sum(trucks_on_bridge) + truck_weights[0] <= weight:
#                 trucks_on_bridge.append(truck_weights.pop(0))
#             else:
#                 trucks_on_bridge.append(0)
#     return answer