# link : https://www.acmicpc.net/problem/11256

case_number = int(input())

test_cases = []
for _ in range(case_number):
    candy_count, box_count = map(int, input().split())
    box_info = []
    for _ in range(box_count):
        x, y = map(int, input().split())
        box_info.append(int(x * y))

    box_info.sort(reverse=True)

    answer = 0
    for box in box_info:
        answer += 1
        if candy_count > box:
            candy_count -= box
        else:
            break

    print(answer)