# link : https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []

    for i in range(len(prices)):
        current_range = prices[i:]
        print(current_range)
        if min(current_range) < current_range[0]:
            print(len(current_range) - current_range.index(min(current_range)))
            answer.append(len(current_range[:current_range.index(min(current_range))]))
        else:
            answer.append(len(current_range) - 1)
    return answer

print(solution([1, 2, 1, 2, 3]))

# Other programmer's solution -- referenced answer
# def solution(prices):
#     answer = [0]*len(prices)
#     stack = []
 
#     for i, price in enumerate(prices):
#         #stack이 비었이면 false
#         while stack and price < prices[stack[-1]]:
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)
 
#     # for문 다 돌고 Stack에 남아있는 값들 pop
#     while stack:
#         j = stack.pop()
#         answer[j] = len(prices) - 1 - j
 
#     return answer