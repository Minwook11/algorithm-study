# link : https://programmers.co.kr/learn/courses/30/lessons/72410
import re

def solution(new_id):
    step_2 = re.compile('([A-Za-z0-9\.\-\_])')
    temp_res = step_2.findall(new_id.lower())

    temp_queue = []
    step_3_flag = 0
    for c in temp_res:
        if step_3_flag == 0:
            if c == '.': 
                step_3_flag = 1
            temp_queue.append(c)
        else: 
            if c == '.' : 
                continue
            else: 
                temp_queue.append(c)
                step_3_flag = 0

    if len(temp_queue) > 1:
        temp_flag = 0
        if temp_queue[0] == '.' : temp_flag += 1
        if temp_queue[-1] == '.': temp_flag += 2

        if temp_flag == 3: temp_queue = temp_queue[1:-1]
        elif temp_flag == 2: temp_queue = temp_queue[:-1]
        elif temp_flag == 1: temp_queue = temp_queue[1:]

    elif len(temp_queue) == 1:
        if temp_queue[0] == '.' : temp_queue.remove('.')

    if len(temp_queue) == 0:
        temp_queue.append('a')

    if len(temp_queue) > 15:
        temp_queue = temp_queue[:15]

    if temp_queue[-1] == '.': temp_queue = temp_queue[:-1]

    for i in range(3):
        if len(temp_queue) <= 2:
            temp_queue.append(temp_queue[-1])
        if len(temp_queue) == 3:
            break

    return ''.join(temp_queue)

print(solution('=.='))

# Other programmer's solution -- Most impressive solution
# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st