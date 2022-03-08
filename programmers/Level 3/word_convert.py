# link : https://programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    if target not in words: return 0
    
    answer = 0
    status = [False] * len(words)
    
    stack = [(begin, 0)]
    
    while stack:
        cur, depth = stack.pop()
        if cur == target:
            answer = depth
            break
        
        for i in range(len(words)):
            if status[i] == True:
                continue
            cnt = 0
            for a,b in zip(cur, words[i]):
                if a!=b:
                    cnt += 1
            if cnt == 1:
                status[i] = True
                stack.append((words[i], depth+1))
    
    return answer