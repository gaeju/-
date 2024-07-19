import math
def solution(n, m, section):
    li = []
    num = 0
    cnt = 0
    for i in section:
      if num <= i:
        cnt += 1
        num = i + m
    return cnt