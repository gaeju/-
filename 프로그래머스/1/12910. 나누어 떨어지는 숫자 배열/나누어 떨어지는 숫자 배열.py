def solution(arr, divisor):
    arr = [i for i in arr if i % divisor == 0]
    if len(arr) > 0: return sorted(arr)
    else: return [-1]