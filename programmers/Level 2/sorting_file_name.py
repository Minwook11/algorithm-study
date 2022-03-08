# link : https://programmers.co.kr/learn/courses/30/lessons/17686

def part_check(word):
    head = ''
    number = ''
    tail = ''

    flag = 0
    for c in word:
        if len(number) == 5: flag = 2
        if flag == 0 and not(c.isdigit()):
            head += c
            continue
        if flag == 0 and c.isdigit():
            flag = 1
            number += c
            continue
        if flag == 1 and c.isdigit():
            number += c
            continue
        if flag == 1 and not(c.isdigit()):
            flag = 2
            tail += c
            continue
        if flag == 2:
            tail += c

    return [head, number, tail]

def solution(s):
    for i in range(len(s) - 1, 0, -1):
        for j in range(i):
            file_1 = part_check(s[j])
            file_2 = part_check(s[j + 1])
            if file_1[0].lower() > file_2[0].lower():
                s[j], s[j + 1] = s[j + 1], s[j]
                continue

            if file_1[0].lower() == file_2[0].lower() and int(file_1[1]) > int(file_2[1]):
                s[j], s[j + 1] = s[j + 1], s[j]
                continue

    return s

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

# Other programmer's solution -- Most simpliest solution
# import re

# def solution(files):
#     a = sorted(files, key=lambda file : int(re.findall('\d{1,5}', file)[0]))
#     b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
#     return b