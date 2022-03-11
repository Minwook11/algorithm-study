# link : https://www.acmicpc.net/problem/2720

quater, dime, nickel, penny = 25, 10, 5, 1

count = int(input())

for _ in range(count):
    payment = int(input())
    
    q = payment // quater
    payment = payment % quater

    d = payment // dime
    payment = payment % dime

    n = payment // nickel
    payment = payment % nickel

    p = payment // penny
    
    print(q, d, n, p)