def solution(food):
    for idx, i in enumerate(food):
        food[idx] = i // 2
        
    answer_1 = ''
    for idx, i in enumerate(food):
        answer_1 += (str(idx) * i)

    answer_2 = ''
    for idx, i in enumerate(food):
        answer_2 += (str(idx) * i)
    
    answer_2 = answer_2[::-1]

    answer = answer_1 + '0' + answer_2
    return answer