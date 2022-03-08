# link : https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key = len)
    for i in s:
        ii = i.split(',')
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

print(solution("{{20,111},{111}}"))

# Other programmer's solution -- Most interesting solution
# def solution(s):
#     s = eval(s.replace("{", "[").replace("}", "]"))
#     answer = list({num:0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
#     return answer