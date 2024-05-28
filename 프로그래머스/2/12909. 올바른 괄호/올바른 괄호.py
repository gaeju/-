def solution(s):
    num = 0
    a, b = 0, 0
    for i in s:
        if i == '(':
            num += 1
            a += 1
        else: 
            num -= 1
            b += 1

        if num < 0:
            return False
    if a != b: return False
    else: return True
  
