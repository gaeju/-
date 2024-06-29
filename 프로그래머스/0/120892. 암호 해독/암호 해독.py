def solution(cipher, code):
    s = ''
    n = 1
    while True:
      s += cipher[(code * n - 1)]
      n += 1
      if len(cipher) < code * n: break
    return s