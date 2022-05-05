# link : https://www.acmicpc.net/problem/15904

input_string = input()

check_stack = []
for single_chr in input_string:
    if len(check_stack) == 0 and single_chr == "U":
        check_stack.append(single_chr)
    if len(check_stack) == 1 and single_chr == "C":
        check_stack.append(single_chr)
    if len(check_stack) == 2 and single_chr == "P":
        check_stack.append(single_chr)
    if len(check_stack) == 3 and single_chr == "C":
        check_stack.append(single_chr)
    
    if len(check_stack) == 4:
        break

if "".join(check_stack) == "UCPC":
    print("I love UCPC")
else:
    print("I hate UCPC")