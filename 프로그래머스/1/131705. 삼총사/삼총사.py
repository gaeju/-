from itertools import combinations
def solution(number):
    n = 0
    for i in combinations(number, 3):
        if sum(i) == 0: n += 1
    return n