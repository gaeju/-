def solution(cards1, cards2, goal):
    li = []
    for i in goal:
        for j in cards1:
            if i == j: li.append(i)
    li2 = [] 
    for i in goal:
        for j in cards2:
            if i == j: li2.append(i)

    if li == cards1[:len(li)] and li2 == cards2[:len(li2)]: return 'Yes'
    else: return 'No'