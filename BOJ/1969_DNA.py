# link : https://www.acmicpc.net/problem/1969

N, M = list(map(int,input().split()))

pre_define_counter = {index : {"A" : 0, "C" :0, "G" : 0, "T" : 0} for index in range(M)}

for _ in range(N):
    input_dna = input()
    for idx, item in enumerate(input_dna):
        pre_define_counter[idx][item] += 1

answer_dna = ""
answer_hamming_value = 0
for key, value in pre_define_counter.items():
    large_char = max(value, key=value.__getitem__)
    value.pop(large_char)
    answer_dna += large_char

    for char, count in value.items():
        answer_hamming_value += count

print(answer_dna)
print(answer_hamming_value)