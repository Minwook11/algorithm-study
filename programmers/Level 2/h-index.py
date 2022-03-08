# link : https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    temp_citations = [ item for item in citations if item > 0]
    if not temp_citations:
        return 0
    ref_counts = sorted(list(set(temp_citations)))

    answer = 0
    for count in range(1, max(citations) + 1):
        if len(temp_citations) < count:
            continue
        else:
            each_count = 0
            for citation in temp_citations:
                if citation >= count:
                    each_count += 1
                if each_count == count:
                    answer = each_count
                    break

    return 'answer is {}'.format(answer)

print(solution([10, 100]))

# Other programmer's solution -- Most Simpliest solution
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer