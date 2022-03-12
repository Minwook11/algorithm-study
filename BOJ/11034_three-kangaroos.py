# link : https://www.acmicpc.net/problem/11034

while True:
    try:
        k1, k2, k3 = map(int, input().split())
        print(max(k2-k1, k3-k2) - 1)
    except:
        break