# link : https://programmers.co.kr/learn/courses/30/lessons/62048

def gcd_cal(num1, num2):
    gcd = 1
    for i in range(1, num1 + 1):
        if (num1 % i == 0) & (num2 % i == 0):
            gcd = i
    return gcd

def solution(w,h):
    if w == 1 or h == 1:
        return 0

    if w == h:
        return (w * h) - w

    cross_point_count = gcd_cal(w, h) - 1
    if cross_point_count == 0:
        return (w * h) - ((w + h) - 1)
    else:
        return (w * h) - ((w + h) - 1 - cross_point_count)

# Other programmer's solution -- Most interesting solution
#def gcd(a,b): return b if (a==0) else gcd(b%a,a)
#def solution(w,h): return w*h-w-h+gcd(w,h)
