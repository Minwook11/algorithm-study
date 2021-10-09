# link : https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    result = 0
    for c in s:
        if c == 'p' or c == 'P':
            result += 1
        elif c == 'y' or c == 'Y':
            result -= 1
        else:
            continue
    return False if result != 0 else True

print(solution('pPoooyY'))

# Other programmer's solution -- Most liked solution
#def numPY(s):
#    # 함수를 완성하세요
#    return s.lower().count('p') == s.lower().count('y')
