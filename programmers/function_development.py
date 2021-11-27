# link : https://programmers.co.kr/learn/courses/30/lessons/42586

def daily_work(progress, speed):
    return progress + speed

def solution(progresses, speeds):
    answer = []

    while(progresses):
        deploy = 0
        progresses = list(map(daily_work, progresses, speeds))

        for progress in progresses:
            if progress < 100: break
            if progress >= 100: deploy += 1

        if deploy > 0:
            answer.append(deploy)
            progresses = progresses[deploy:]
            speeds = speeds[deploy:]

    return answer

# Other programmer's solution == Most liked soultion
#def solution(progresses, speeds):
#    Q=[]
#    for p, s in zip(progresses, speeds):
#        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#            Q.append([-((p-100)//s),1])
#        else:
#            Q[-1][1]+=1
#    return [q[1] for q in Q]
