def solution(babbling):
    li = ["aya", "ye", "woo", "ma"]
    for i in li:
      for idx, j in enumerate(babbling):
        if i * 2 in j: 
          continue
        if i in j:
          babbling[idx] = j.replace(i, ' ')

    for idx, j in enumerate(babbling):
      babbling[idx] = j.replace(' ', '')


    return babbling.count('')