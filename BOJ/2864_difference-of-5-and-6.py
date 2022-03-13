# link : https://www.acmicpc.net/problem/2864

def find_num(num_string):
    high, low = list(num_string), list(num_string)

    for i in range(len(num_string)):
        if '5' == num_string[i] or '6' == num_string[i]:
            high[i] = '6'
            low[i] = '5'
    return int(''.join(high)), int(''.join(low))

n1, n2 = input().split()

n1_high, n1_low = find_num(n1)
n2_high, n2_low = find_num(n2)

print(n1_low + n2_low, n1_high + n2_high)