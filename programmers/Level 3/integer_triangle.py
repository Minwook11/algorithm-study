# https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += triangle[i+1][j+1] if triangle[i+1][j+1] > triangle[i+1][j] else triangle[i+1][j]
            
    return triangle[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))