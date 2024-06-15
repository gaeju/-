def solution(n):
    li = []
    for i in range(n+1): 
        if i % 2 != 0:
            li.append(i)
    return li