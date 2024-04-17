# link : https://www.acmicpc.net/problem/20310

S = input()

chr_count = {
    "0" : 0,
    "1" : 0
}

for i in S:
    chr_count[i] += 1

temp = ""
cnt_0, cnt_1 = 0, 0
for i in S:
    if cnt_1 != chr_count["1"] // 2:
        if i == "1":
            cnt_1 += 1
            pass
        else:
            temp += i
    else:
        temp += i

answer = ""
for i in reversed(temp):
    if cnt_0 != chr_count["0"] // 2:
        if i == "0":
            cnt_0 += 1
            pass
        else:
            answer += i
    else:
        answer += i

print(answer[::-1])