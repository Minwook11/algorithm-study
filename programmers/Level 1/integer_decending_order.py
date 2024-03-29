# link : https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))

print(solution(118372))

# Other programmer's solution -- Most interested soultion
#def merge(left, right):
#    result = []
#    while len(left) > 0 or len(right) > 0:
#        if len(left) > 0 and len(right) > 0:
#            if left[0] >= right[0]:
#                result.append(left[0])
#                left = left[1:]
#            else:
#                result.append(right[0])
#                right = right[1:]
#        elif len(left) > 0:
#            result.append(left[0])
#            left = left[1:]
#        elif len(right) > 0:
#            result.append(right[0])
#            right = right[1:]
#    return result
#
#def mergeSort(arr):
#    if len(arr) <= 1:
#        return arr
#
#    mid = len(arr) // 2
#    left = arr[:mid]
#    right = arr[mid:]
#
#    left = mergeSort(left)
#    right = mergeSort(right)
#
#    return merge(left, right)
#
#def solution(n):
#    arr = list(str(n))
#    n = int(''.join(mergeSort(arr)))
#    return n
