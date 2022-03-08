# link : https://programmers.co.kr/learn/courses/30/lessons/72412

def solution(info, queries):
    answer = []
    for query in queries:
        query = query.split(' ')
        c1, c2, c3, c4, c5 = query[0], query[2], query[4], query[6], query[7]
        count = 0

        for applicant in info:
            check_status = 0
            applicant = applicant.split(' ')
            if c1 == '-' or applicant[0] == c1:
                check_status = 1
            else:
                continue

            if c2 == '-' or applicant[1] == c2:
                check_status = 2
            else:
                continue

            if c3 == '-' or applicant[2] == c3:
                check_status = 3
            else:
                continue

            if c4 == '-' or applicant[3] == c4:
                check_status = 4
            else:
                continue

            if c5 == '-' or int(applicant[4]) >= int(c5):
                check_status = 5
            else:
                continue

            if check_status == 5:
                count += 1

        answer.append(count)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210",
"python frontend senior chicken 150","cpp backend senior pizza 260",
"java backend junior chicken 80","python backend senior chicken 50"], 
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250","- and backend and senior and - 150",
"- and - and - and chicken 100","- and - and - and - 150"]))

# Other programmer's solution -- Efficiency check passed solution
# solution link : https://dev-note-97.tistory.com/131
# from itertools import combinations
# def solution(info, query):
#     answer = []
#     db = {}
#     for i in info:                   # info에 대해 반복
#         temp = i.split()
#         conditions = temp[:-1]       # 조건들만 모으고, 점수 따로
#         score = int(temp[-1])  
#         for n in range(5):           # 조건들에 대해 조합을 이용해서  
#             combi = list(combinations(range(4), n))
#             for c in combi:
#                 t_c = conditions.copy()
#                 for v in c:          # '-'를 포함한 새로운 조건을 만들어냄.
#                     t_c[v] = '-'
#                 changed_t_c = '/'.join(t_c)
#                 if changed_t_c in db:     # 모든 조건의 경우에 수에 대해 딕셔너리
#                     db[changed_t_c].append(score)
#                 else:
#                     db[changed_t_c] = [score]

#     for value in db.values():             # 딕셔너리 내 모든 값 정렬
#         value.sort()
 
#     for q in query:                       # query의 모든 조건에 대해서
#         qry = [i for i in q.split() if i != 'and']
#         qry_cnd = '/'.join(qry[:-1])
#         qry_score = int(qry[-1])
#         if qry_cnd in db:                 # 딕셔너리 내에 값이 존재한다면,
#             data = db[qry_cnd]
#             if len(data) > 0:          
#                 start, end = 0, len(data)     # lower bound 알고리즘 통해 인덱스 찾고,
#                 while start != end and start != len(data):
#                     if data[(start + end) // 2] >= qry_score:
#                         end = (start + end) // 2
#                     else:
#                         start = (start + end) // 2 + 1
#                 answer.append(len(data) - start)      # 해당 인덱스부터 끝까지의 갯수가 정답
#         else:
#             answer.append(0)

#     return answer