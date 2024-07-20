def solution(str_list, ex):
    s = ''
    for i in str_list:
        if ex not in i: s += i

    return s