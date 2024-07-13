def solution(n, k):
    answer = list(range(1, n + 1))
    return answer[k-1::k]