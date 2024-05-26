def solution(arr):
    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    answer = arr[0]
    for i in range(len(arr)):
        answer = lcm(answer, arr[i])
    return answer