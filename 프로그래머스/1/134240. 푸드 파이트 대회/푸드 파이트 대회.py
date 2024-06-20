def solution(food):
    answer = ''
    for idx, i in enumerate(food):
        answer += (str(idx) * int(i//2))
    answer = answer + '0' + answer[::-1]
    
    return answer