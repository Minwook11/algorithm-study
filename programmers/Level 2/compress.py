# link : https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    comp_dic = { chr(65 + i) : i + 1 for i in range(26) }

    for i in range(26):
        comp_dic[chr(65+i)] = i+1

    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(comp_dic[msg[w:c]])
            break
        if msg[w:c+1] not in comp_dic:
            comp_dic[msg[w:c+1]] = len(comp_dic) + 1
            answer.append(comp_dic[msg[w:c]])
            w = c

    return answer

print(solution('KAKAO'))

# Other programmer's solution -- Most interesting solution
# def solution(msg):
#     answer = []
#     tmp = {chr(e + 64): e for e in range(1, 27)}
#     num = 27
#     while msg:
#         tt = 1
#         while msg[:tt] in tmp.keys() and tt <= msg.__len__():
#             tt += 1
#         tt -= 1
#         if msg[:tt] in tmp.keys():
#             answer.append(tmp[msg[:tt]])
#             tmp[msg[:tt + 1]] = num
#             num += 1
#         msg = msg[tt:]
#     return answer