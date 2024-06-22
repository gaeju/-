def solution(nums):
    cnt = len(nums) // 2
    if len(set(nums)) <= cnt: return len(set(nums))
    else: return cnt