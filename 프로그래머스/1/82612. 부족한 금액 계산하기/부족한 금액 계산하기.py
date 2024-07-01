def solution(price, money, count):
    s = 0
    for i in range(1, count + 1):
        s += price * i

    if s - money > 0: return s-money
    else: return 0