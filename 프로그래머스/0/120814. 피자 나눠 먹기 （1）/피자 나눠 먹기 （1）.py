def solution(n):
    cnt = 1
    while True:
        if 7 * cnt / n >= 1:
            break
        else: cnt += 1
    return cnt