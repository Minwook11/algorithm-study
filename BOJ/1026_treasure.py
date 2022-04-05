# link : https://www.acmicpc.net/problem/1026

length = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
A.sort()
B.sort(reverse=True)
for i in range(length):
    answer += int(B[i] * A[i])

print(answer)