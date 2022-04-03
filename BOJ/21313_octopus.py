# link : https://www.acmicpc.net/problem/21313

octopus_num = int(input())

ans = [1, 2] * (octopus_num // 2) + ([3] if octopus_num % 2 else [])

print(*ans)