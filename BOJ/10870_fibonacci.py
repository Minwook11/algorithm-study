# link : https://www.acmicpc.net/problem/10870

def recursion(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return recursion(n - 1) + recursion(n - 2)

base_num = int(input())

print(recursion(base_num))