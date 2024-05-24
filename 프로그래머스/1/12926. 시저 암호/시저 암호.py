def solution(s, n):
    s = [i for i in s]
    alpha = [i for i in 'abcdefghijklmnopqrstuvwxyz']
    string = ''
    for i in range(n):
        alpha.append(alpha[i])

    for i in s:
        if i.lower() in alpha:
            index_num = alpha.index(i.lower())
            if i == i.lower():
                string += alpha[index_num+n]
            else: 
                string += alpha[index_num+n].upper()
        else: string += ' '
    
    return string