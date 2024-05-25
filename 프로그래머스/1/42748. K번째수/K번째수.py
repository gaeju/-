def solution(array, commands):
    answer = []
    for a in commands:
        i, j, k = a[0], a[1], a[2]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer