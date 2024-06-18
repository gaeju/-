def solution(x):
    s_0 = 0
    cnt = 0
    while True:
        if x =='1':
            break
        s_0 += x.count('0')
        x = x.replace('0','')
        x = bin(len(x))[2:]
        cnt += 1

    answer = [cnt,s_0]
    return answer