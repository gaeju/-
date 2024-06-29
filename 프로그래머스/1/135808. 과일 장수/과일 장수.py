def solution(k, m, score):
    score.sort(reverse=True)
    s = 0
    n = 1
    for i in range(len(score) // m):
      s += min(score[m*n-m:m*n]) * m
      n += 1
    return s