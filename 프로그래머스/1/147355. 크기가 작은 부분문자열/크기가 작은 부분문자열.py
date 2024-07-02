def solution(t, p):
    n = 0
    for i in range(len(t) - len(p) + 1):
        if t[i:i+len(p)] <= p: n += 1 
    return n