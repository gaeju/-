def solution(arr):
    if len(arr) <= 1: answer = [-1]
    else:
        min_num = arr.index(min(arr))
        arr.pop(min_num)
        answer = arr
    return answer