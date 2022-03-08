# link : https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort()
    answer = 0

    while people:

        heaviest = people.pop(-1)
        if people:
            if heaviest + people[0] > limit:
                answer += 1
            else:
                if people:
                    people.pop(0)
                answer += 1
        else:
            answer += 1

    return answer

print(solution([70, 50, 80], 100))

# Other programmer's solution -- Referenced Answer
# def solution(people, limit) :
#     answer = 0
#     people.sort()

#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer