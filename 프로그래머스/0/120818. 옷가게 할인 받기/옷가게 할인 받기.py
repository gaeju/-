def solution(price):
    if price >= 500000:
        sale = 20
    elif price >= 300000:
        sale = 10
    elif price >= 100000:
        sale = 5
    else: sale = 0

    answer = int(price * (100 - sale) * 0.01)
    return answer