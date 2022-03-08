# link : https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = []
    print(s.split(' '))
    for word in s.split(' '):
        if word:
            if word[0].isdigit():
                answer.append(word)
            else:
                answer.append(word[0].upper() + word[1:].lower()) if len(word) > 1 else answer.append(word.upper())
        
        answer.append(' ')
    return ''.join(answer)[:-1]

print(solution('for the last week'))