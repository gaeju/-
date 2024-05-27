def solution(clothes):
    dic = {}
    for i in clothes:
        dic[i[1]] = 1

    for i in clothes:
        dic[i[1]] += 1
        
    mul = 1
    for i in dic.values():
        mul *= i
    return mul - 1