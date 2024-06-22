def solution(name, yearning, photo):
    name_score = dict(zip(name,yearning))
    li = []
    for i in photo:
        s = 0
        for j in i:
            try: s += name_score[j]
            except: pass
        li.append(s)
    return li