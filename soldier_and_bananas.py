k, n, w = map(int, input().split())

value = (1 + w) * w/2
prices = value * k

if n >= prices:
    print(0)
else:
    print(int(prices - n))
