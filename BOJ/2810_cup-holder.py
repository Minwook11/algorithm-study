# link : https://www.acmicpc.net/problem/2810

seat_num = int(input())
seat_setting = input()

holder_count = 1
couple_flag = False
for i in range(len(seat_setting)):
    if not couple_flag:
        if seat_setting[i] == 'S' :
            holder_count += 1
        else:
            couple_flag = True
            holder_count += 1
    else:
        couple_flag = False

answer = holder_count if holder_count < seat_num else seat_num
print(answer)