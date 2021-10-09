# link : https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return "김서방은 {}에 있다".format(i)
    return False

print(solution(['Jane','Kim']))

# Other programmer's solution -- Most liked soultion
#def findKim(seoul):
#    return "김서방은 {}에 있다".format(seoul.index('Kim'))
