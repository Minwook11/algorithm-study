# link : https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    user_record = {}
    answer = []
    message_queue = []
    
    for single_record in record:
        split_record = single_record.split()
    
        if len(split_record) == 3:
            user_record[split_record[1]] = split_record[2]
        
        if split_record[0] == 'Enter':
            message_queue.append({
                'Enter' : split_record[1]
            })
        elif split_record[0] == 'Leave':
            message_queue.append({
                'Leave' : split_record[1]
            })
    for message in message_queue:
        if message.get('Enter'):
            answer.append("{}님이 들어왔습니다.".format(user_record[message['Enter']]))
        elif message.get('Leave'):
            answer.append("{}님이 나갔습니다.".format(user_record[message['Leave']]))
    
    return answer

# Other programmer's solution -- Most simple solution
#def solution(record):
#    answer = []
#    namespace = {}
#    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
#    for r in record:
#        rr = r.split(' ')
#        if rr[0] in ['Enter', 'Change']:
#            namespace[rr[1]] = rr[2]
#
#    for r in record:
#        if r.split(' ')[0] != 'Change':
#            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])
#
#    return answer
