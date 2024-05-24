def solution(s):
    answer = ''
    s_list = s.split(' ')
    for a in s_list:
        s_1 = [i for i in a]
        for i in range(len(s_1)):
            if i % 2 == 0: s_1[i] = s_1[i].upper()
            else: s_1[i] = s_1[i].lower()
        answer += ''.join(s_1) + ' '
    return answer[:-1]