import string
tmp = string.digits+string.ascii_lowercase
def convert(n) :
    q, r = divmod(n, 3)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q) + tmp[r]
    
def solution(n):
    string = convert(n)[::-1]
    return int(string, 3)