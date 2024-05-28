def solution(progresses, speed):
    answer = []
    li = []
    while True:
        progresses = [x + y for x, y in zip(progresses,speed)]
        if progresses[0] >= 100:
            li = []
            for idx, i in enumerate(progresses):
                if i < 100:
                    break
                
                li.append(progresses[0])
                progresses = progresses[1:]
                speed = speed[1:]
            answer.append(len(li))

        if len(progresses) == 0:
            break
    return answer