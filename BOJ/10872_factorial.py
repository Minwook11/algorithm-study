# link : https://www.acmicpc.net/problem/10872

def recursion(n):
    if n == 0:
        return 1

    if n == 1:
        return 1

    return n * recursion(n - 1)

print(recursion(int(input())))