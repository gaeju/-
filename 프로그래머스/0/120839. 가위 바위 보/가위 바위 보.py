def solution(rsp):
    string = ''
    for i in rsp:
        if i == '2': string += '0'
        elif i == '0': string += '5'
        else: string += '2'
    return string