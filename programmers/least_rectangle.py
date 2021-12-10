# link : https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    least_x = 0
    least_y = 0

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i] = sorted(sizes[i], reverse = True)

        if sizes[i][0] > least_x: least_x = sizes[i][0]
        if sizes[i][1] > least_y: least_y = sizes[i][1]

    return least_x * least_y

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

# Other programmer's solution
# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)