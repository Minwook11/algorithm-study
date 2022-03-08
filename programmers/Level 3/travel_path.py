# link : https://programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# Other programmer's solution -- Most interesting solution, used default dict
# from collections import defaultdict

# def solution(tickets):
#     answer = []
#     routes = defaultdict(list)

#     for ticket in tickets:
#         routes[ticket[0]].append(ticket[1])

#     for key in routes.keys():
#         routes[key].sort(reverse=True)

#     stack = ['ICN']
#     while stack:
#         tmp = stack[-1]

#         if not routes[tmp]:
#             answer.append(stack.pop())
#         else:
#             stack.append(routes[tmp].pop())
#     answer.reverse()

#     return answer