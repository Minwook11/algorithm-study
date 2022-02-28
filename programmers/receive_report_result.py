
def solution(id_list, report, k):
    report = list(set(report))

    res = { id : []  for id in id_list }
    for single in report:
        temp = single.split(' ')
        res[temp[1]].append(temp[0])

    temp_list = []
    for single in res.values():
        if len(single) >= k: temp_list += single

    answer = [ temp_list.count(id) for id in id_list ]

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

# Other programmer's solution -- Most simpliest solution
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer