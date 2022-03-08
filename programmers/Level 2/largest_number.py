# link : https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = list(map(str,numbers)) 
    numbers.sort(key=lambda x: x * 3, reverse=True) 
    if sum(list(map(int,numbers))) == 0:
    	numbers = list(set(numbers))
    return "".join(numbers)

# Other programmer's solution -- Most liked solution
#def solution(numbers):
#    numbers = list(map(str, numbers))
#    numbers.sort(key=lambda x: x*3, reverse=True)
#    return str(int(''.join(numbers)))
