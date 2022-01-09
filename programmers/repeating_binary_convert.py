# link : https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    if s == '1' : return [0, 0]
    depth_count, zero_count = 0, 0

    while True:
        depth_count += 1
        current_zero = s.count('0')
        zero_count += current_zero

        s = ''.join(['1' for _ in range(s.count('1'))])

        if s == '1':
            break
        else:
            s = bin(len(s))[2:]

    return [depth_count, zero_count]

print(solution("110010101001"))