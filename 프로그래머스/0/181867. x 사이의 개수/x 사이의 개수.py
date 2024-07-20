def solution(myString):
    li = []
    for i in myString.split('x'):
        li.append(len(i))
    return li
