# link : https://www.acmicpc.net/problem/15881

n = int(input())
 
arr = list(input())
 
arr.extend([0] * 1000000)
 
i, cnt = 0, 0
 
while(i < n):
    if(arr[i] == 'p' and arr[i+1] == 'P' and arr[i+2] == 'A' and arr[i+3] == 'p'):
        arr[i+3] = 0
        cnt += 1
    i += 1
 
print(cnt)