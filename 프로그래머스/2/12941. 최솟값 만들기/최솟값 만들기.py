def solution(a, b):
    s = 0
    a = sorted(a)
    b = sorted(b, reverse=True)
    for i in range(len(a)):
        s += a[i] * b[i]

    return s