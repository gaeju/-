def solution(money):
    coffee = 5500

    cnt = money // coffee
    change = money % coffee
    answer = [cnt, change]
    return answer