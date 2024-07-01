def solution(absolutes, signs):
    s = 0
    for i in range(len(signs)):
        if signs[i] == True: sign = 1
        else: sign = -1
        s += sign * absolutes[i]
    return s