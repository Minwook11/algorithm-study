# link : https://www.acmicpc.net/problem/4796

input_conditions = []
while True:
    temp_data = list(map(int, input().split()))
    if temp_data[0] == 0 and temp_data[1] == 0 and temp_data[2] == 0:
        break
    else:
        input_conditions.append(temp_data)
    
for case, conditions in enumerate(input_conditions):
    res = ((conditions[2] // conditions[1]) * conditions[0])
    res += min(conditions[2] % conditions[1], conditions[0])
    print('Case {}: {}'.format(case + 1, res))