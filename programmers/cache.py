# link ; https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    answer = 0
    cache = []

    for city in cities:
        l_city = city.lower()
        if l_city in cache:
            cache.remove(l_city)
            cache.append(l_city)
            answer += 1
        else:
            answer += 5
            cache.append(l_city)
            if len(cache) > cacheSize: cache = cache[1:]

    return answer

print(solution(5, ["Jeju", "Jeju",]))

# Other programmer's solution
# def solution(cacheSize, cities):
#     import collections
#     cache = collections.deque(maxlen=cacheSize)
#     time = 0
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             time += 1
#         else:
#             cache.append(s)
#             time += 5
#     return time