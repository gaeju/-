import itertools
def solution(nums):
    num = 0
    for i in list(itertools.combinations(nums, 3)):
      n = 0
      for j in range(1, sum(i)+1):
        if sum(i) % j == 0: n += 1
      if n <= 2: num += 1

    return num