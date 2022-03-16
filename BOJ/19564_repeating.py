# link : https://www.acmicpc.net/problem/19564

word = [ ord(i) for i in list(input()) ]

answer = 0
check = word[0]

for i in range(1, len(word)):
    if check >= word[i]:
        answer += 1
    check = word[i]

print(answer + 1)