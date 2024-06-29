def solution(my_string):
    s = ''
    for i in my_string:
      if i == i.lower():
        s += i.upper()
      else: s += i.lower()
    return s