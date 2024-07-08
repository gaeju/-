def solution(myString, pat):
    string = myString.replace('A', 'a').replace('B', 'b').replace('a', 'B').replace('b', 'A')
    if pat in string: 
        return 1
    else: 
        return 0
