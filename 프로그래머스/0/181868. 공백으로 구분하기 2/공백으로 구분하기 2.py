def solution(my_string):
    answer = []
    string = my_string.split(' ')
    for i in string:
        if i != '': answer.append(i)
    return answer