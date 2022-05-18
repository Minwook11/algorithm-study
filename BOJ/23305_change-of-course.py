# link : https://www.acmicpc.net/problem/23305

student_num = int(input())

registered = list(map(int, input().split()))
wanted = list(map(int, input().split()))

temp_dict = dict()
for item in registered:
    if item in temp_dict:
        temp_dict[item] += 1
    else:
        temp_dict[item] = 1

count = 0
for item in wanted:
    if item in temp_dict:
        if temp_dict[item] > 0:
            count += 1
            temp_dict[item] -= 1

print(student_num - count)