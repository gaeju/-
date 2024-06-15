def solution(array):
    array = sorted(array)
    num = int((len(array) + 1) / 2 - 1)
    answer = array[num]
    return answer