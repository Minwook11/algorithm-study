# link : https://programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    chr_list = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    target = len(word)
    repeat_crit = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1
    for i in word:
        target += repeat_crit * chr_list[i]
        repeat_crit = (repeat_crit - 1) // 5
    return target

print(solution('I'))