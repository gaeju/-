def solution(arr):
    answer = []
    for i in range(len(arr)):
        try: 
            if answer[-1] != arr[i]: answer.append(arr[i])
        except: answer.append(arr[i])
    return answer