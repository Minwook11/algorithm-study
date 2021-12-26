# link : https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]

    count = 0
    for word in words[1:]:
        count += 1
        if word in words[:count - 1] or word[0] != words[count - 1][-1]:
            answer[0] = (count % n) + 1
            answer[1] = (count // n) + 1
            break
        
    return answer

print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))