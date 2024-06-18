def solution(n):
    cnt = 0
    for i in range(1, n + 1):
        result = 0
        for j in range(i, n+1, 1):
          # print(result, j, result + j)
            result += j
            if result >= n:
                break 
      # print(result)
        if result == n:
            cnt +=1

    return cnt