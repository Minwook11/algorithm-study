# link : https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    week_day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = sum(days_in_month[:a - 1]) + b + 4

    return week_day[days % 7]

print(solution(5, 24))
