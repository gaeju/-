def solution(numbers):
    li = []
    for idx_i, i in enumerate(numbers):
      for idx_j, j in enumerate(numbers):
        if idx_i == idx_j: pass
        else:
          li.append(i + j)

    answer = sorted(list(set(li)))

    return answer