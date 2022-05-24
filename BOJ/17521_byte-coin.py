# link : https://www.acmicpc.net/problem/17521

trade_day, cash = map(int, input().split())
price_info = [ int(input()) for _ in range(trade_day) ]

coin = 0
for i in range(trade_day - 1):
    if price_info[i] < price_info[i+1] :
        if cash // price_info[i] > 0 :
            coin = cash // price_info[i]
            cash -= price_info[i] * coin
    elif price_info[i] > price_info[i-1] :
            cash += price_info[i] * coin
            coin = 0

if coin > 0:
    cash += coin * price_info[-1]

print(cash)