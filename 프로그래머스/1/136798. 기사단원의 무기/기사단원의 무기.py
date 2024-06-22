def devisor(i):
  li = []
  for j in range(1, int(i**0.5) + 1):
    if i % j == 0: 
      li.append(j)
      if j != i // j: 
        li.append(i // j)
  return li

def solution(number, limit, power): 
    li = []
    knight = range(1, number + 1)
    for i in knight:
      d = devisor(i)
      li.append(len(d))

    for idx, i in enumerate(li):
      if i > limit: li[idx] = power

    return sum(li)