# link : https://programmers.co.kr/learn/courses/30/lessons/17677

def preprocess(word):
    word = word.upper()
    temp = []
    for i in range(len(word) - 1):
        if word[i].isalpha() and word[i+1].isalpha():
            temp.append(f"{word[i]}{word[i+1]}")
    return temp


def solution(str1, str2):
    split_1, split_2 = preprocess(str1), preprocess(str2)
    if len(split_1) == len(split_2) == 0:
        return 65536
    
    long = split_1 if len(split_1) >= len(split_2) else split_2
    short = split_1 if len(split_1) < len(split_2) else split_2

    union = [ item for item in short if item not in long] + long
    intersection = []
    for item in short:
        if item in long:
            intersection.append(long.pop(long.index(item)))


    return int((len(intersection) / len(union)) * 65536)

print(solution("aaabb", "aabbb"))

# Other programmer's solution -- Reference solution
# import math


# def solution(str1, str2):
#     s1 = make_2_word(str1)
#     s2 = make_2_word(str2)
#     print(s1,s2)
#     if s1 == [] and s2 == []:
#         return 65536

#     s1_copy = s1.copy()
#     s2_copy = s2.copy()

#     # 교집합
#     inter = []
#     for i in s1:
#         if i in s2_copy:
#             inter.append(i)
#             s1_copy.remove(i)
#             s2_copy.remove(i)


#     # 합집합
#     union = inter + s1_copy + s2_copy


#     answer = math.floor((len(inter) / len(union)) * 65536)
#     return answer


# def make_2_word(s):
#     s = s.upper()
#     a = []
#     for i in range(len(s) - 1):
#         if s[i:i + 2].isalpha():
#             a.append(s[i:i + 2])
#     return a