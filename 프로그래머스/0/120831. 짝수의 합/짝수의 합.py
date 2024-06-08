def solution(n): # n = [1,2,3,4,5,6,7,8,9,10]
    s = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            s += i
    return s