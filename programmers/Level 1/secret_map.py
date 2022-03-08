# link : https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    data_compare = lambda x, y: '#' if (int(x) or int(y)) == True else ' '
    length_check = lambda x: [ '0' for i in range(n - len(x))] + x if len(x) != n else x

    for data_1, data_2 in zip(arr1, arr2):
        binary_1, binary_2 = length_check(list(bin(data_1))[2:]), length_check(list(bin(data_2))[2:])
        
        temp_data = [ data_compare(x, y) for x, y in zip(binary_1, binary_2) ]
        answer.append(''.join(temp_data))

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

# Other programmer's solution -- Most Simpliest solution(Using Bit Compare)
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer