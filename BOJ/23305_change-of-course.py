# link : https://www.acmicpc.net/problem/23305

student_num = int(input())

registered = list(map(int, input().split()))
wanted = list(map(int, input().split()))

temp_data = sorted(registered + wanted)
count, index = 0, 0
while True:
    if temp_data[index] == temp_data[index + 1]:
        count += 1
        index += 2
    else:
        index += 1

    if index >= len(temp_data) - 1:
        break

print((len(temp_data) // 2) - count)