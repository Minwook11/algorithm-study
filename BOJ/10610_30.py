# link : https://www.acmicpc.net/problem/10610
input_num = list(input())

if "0" not in input_num:
    print(-1)
else:
    input_num.sort(reverse=True)
    multiply_check = sum([ int(i) for i in input_num ] )
    if multiply_check % 3 != 0:
        print(-1)
    else:
        print(''.join(input_num))