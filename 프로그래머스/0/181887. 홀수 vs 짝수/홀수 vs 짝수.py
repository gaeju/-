def solution(num_list):
    even, odd = 0, 0
    for idx, i in enumerate(num_list):
        if idx % 2 == 0:
            even += i
        else: odd += i
    
    if even >= odd: return even
    else: return odd