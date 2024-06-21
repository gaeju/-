def solution(n, arr1, arr2):
    def to_bin(arr1, n):
      for idx, i in enumerate(arr1):
        if len(bin(i)[2:]) < n:
          arr1[idx]='0' * (n - len(bin(i)[2:])) + bin(i)[2:]
        else: arr1[idx]=bin(i)[2:]
      return arr1

    arr1, arr2 = to_bin(arr1, n), to_bin(arr2, n)

    arr = []

    for i in range(n):
      s = ''
      for j in range(n):
        if arr1[i][j] == '0' and arr2[i][j] == '0': s += '0'
        else: s += '1'
      s = s.replace('1', '#').replace('0', ' ')
      arr.append(s)
    return arr