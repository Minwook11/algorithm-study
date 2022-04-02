# link : https://www.acmicpc.net/problem/17224

base_setting = list(map(int, input().split()))

question_list = []

for _ in range(base_setting[0]):
    question_list.append(list(map(int, input().split())))

question_list.sort(key=lambda x: x[1])

result = []
for question in question_list:
    if question[1] <= base_setting[1]:
        result.append(140)
        continue
    if question[0] <= base_setting[1]:
        result.append(100)
        continue

last_index = len(result) if len(result) <= base_setting[2] else base_setting[2]
print(sum(result[:last_index]))