def solution(d, budget):
  d = sorted(d)
  n = len(d)
  while True:
    if sum(d) <= budget:
      return len(d)
    d = d[:-1]  