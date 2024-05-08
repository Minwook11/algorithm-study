# link : https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n , puddles):
    coordinate = []
    for _ in range(n):
        coordinate.append([1] * m)

    puddles = [[puddle[1]-1, puddle[0]-1] for puddle in puddles]
    
    for x in range(0, m):
        for y in range(0, n):
            # print(y, x)
            if x==0 and y==0:
                pass
            elif x==0:
                if [y, x] in puddles:
                    # print("puddle")
                    coordinate[y][x] = 0
                else:
                    coordinate[y][x] = coordinate[y-1][x]
            elif y==0:
                if [y, x] in puddles:
                    # print("puddle")
                    coordinate[y][x] = 0
                else:
                    coordinate[y][x] = coordinate[y][x-1]
            else:
                if [y, x] in puddles:
                    # print("puddle")
                    coordinate[y][x] = 0
                else:
                    coordinate[y][x] = coordinate[y-1][x] + coordinate[y][x-1]
            # print(coordinate)
        # print("--")
    return coordinate[n-1][m-1] % 1000000007


print(solution(4, 3, [[1,2]]))