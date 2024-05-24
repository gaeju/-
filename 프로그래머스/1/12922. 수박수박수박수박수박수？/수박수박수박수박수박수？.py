def solution(n):
    a, b = '수', '박'
    string = ''
    for i in range(n):
        if i % 2 == 0: string = string + a
        else: string = string + b
    return string