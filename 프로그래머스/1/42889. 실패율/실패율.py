def solution(N, stages):
    dic = {}
    for i in range(1, N+1):
        if len(stages) != 0:
            dic[i] = stages.count(i)/len(stages)
            if i in stages:
                stages = [j for j in stages if i != j]
        else: dic[i] = 0
    dic = sorted(dic.items(), key=lambda x:x[1], reverse = True)
    return [i[0] for i in dic]
    