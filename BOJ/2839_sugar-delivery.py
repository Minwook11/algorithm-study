# link : https://www.acmicpc.net/problem/2839

amount = int(input())

answer = -1
for i in range((amount // 5) + 1):
    temp_answer, temp_amount = i, amount - (5 * i) if amount >= 5 else  amount

    temp_answer += temp_amount // 3
    if temp_amount % 3 == 0:
        if answer == -1: answer = temp_answer
        elif answer > temp_answer: answer = temp_answer

print(answer)