def solution(a, b, n):
    cola = 0
    bottle = 0 
    answer = 0

    cnt = 0
    while True:
      cola = (n + bottle) // a * b 
      bottle = (n + bottle) % a  
      n = cola 
      answer += n
      if n == 0:#cola <= 1 and bottle == 0:
        break
    return answer