# link : https://www.acmicpc.net/problem/1817 

N, M = list(map(int,input().split()))
if N == 0: 
    print(0)
else:
    answer = 0
    current_weight = 0
    cargo_list = [ int(cargo) for cargo in input().split()]

    count = 0
    while True:
        count += 1
        cargo = cargo_list.pop(0)
        current_weight += cargo
        if current_weight > M:
            answer += 1
            current_weight = cargo
        elif current_weight == M:
            answer += 1
            current_weight = 0
        else:
            pass

        if count == N:
            break

    if current_weight > 0:
        answer += 1

    print(answer)