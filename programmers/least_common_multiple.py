# link : https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    arr.sort(reverse=True)
    answer = 0

    count = 1
    max_val = max(arr)
    while True:
        check = max_val * count

        flag = True
        for i in arr[1:]:
            if check % i != 0:
                flag = False
                break

        if flag:
            answer = check
            break
        count += 1
    return answer

print(solution([2, 6, 8, 14]))