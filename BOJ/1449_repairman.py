# link : https://www.acmicpc.net/problem/1449

N, L = list(map(int,input().split()))

pipe_status = sorted(list(map(int,input().split())))

answer = 0
current = 1
while True:
    if current in pipe_status:
        answer += 1
        current += L
    else:
        current += 1

    # 반복문 탈출 조건
    # 현재 확인하는 파이트 위치가 문제 위치 중 가장 멀리있는 지점보다 클 경우(문제 위치 지점은 정렬이 가능)
    if current > max(pipe_status):
        break
    # 사용된 테이프 수가 문제 위치 개수와 같은 경우(최악의 경우)
    if answer == len(pipe_status):
        break

print(answer)