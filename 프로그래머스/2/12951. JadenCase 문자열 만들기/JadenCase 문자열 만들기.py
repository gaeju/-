def solution(s):
    s_list = s.split(' ')
    s_list
    answer = ''
    for i in s_list:
        if i != '':
            answer += i[0].upper() + i[1:].lower() + ' '
        else: answer += ' '
        
    return answer[:-1]