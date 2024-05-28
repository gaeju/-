def solution(s):
    try:
        s1 = s[1:-1].split('},{')
        for i in range(len(s1)):
            if '{' in s1[i]:
                s1[i] = s1[i][1:]
            elif '}' in s1[i]:
                s1[i] = s1[i][:-1]

        s1.sort(key=len)

        li = []
        for i in s1:
            li.append(i.split(','))

        a = li[0] # [2] 
        for i in range(len(li)):
            b = li[i] #[2]
            x = [x for x in b if x not in a] #[]
            if len(x) >= 1:
                a.append(x[0])

        answer = []
        for i in a:
            answer.append(int(i))
        return answer

    except: 
        answer = []
        answer.append(int(s[2:-2]))
        return answer