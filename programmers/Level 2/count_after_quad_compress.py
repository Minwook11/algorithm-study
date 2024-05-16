# link : https://school.programmers.co.kr/learn/courses/30/lessons/68936
def solution(arr):
    n = len(arr)

    def count_same(x, y, size):
        initial = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != initial:
                    return False, initial
        return True, initial

    def compress(x, y, size):
        if size == 1:
            return (1, 0) if arr[x][y] == 0 else (0, 1)

        is_same, value = count_same(x, y, size)
        if is_same:
            return (1, 0) if value == 0 else (0, 1)

        half_size = size // 2
        result1 = compress(x, y, half_size)
        result2 = compress(x, y + half_size, half_size)
        result3 = compress(x + half_size, y, half_size)
        result4 = compress(x + half_size, y + half_size, half_size)

        zero_count = result1[0] + result2[0] + result3[0] + result4[0]
        one_count = result1[1] + result2[1] + result3[1] + result4[1]

        return [zero_count, one_count]

    return compress(0, 0, n)

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))