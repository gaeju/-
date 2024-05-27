citations = [9, 7, 6, 2, 1]
def solution(citations): 
    citations = sorted(citations, reverse=True)
    citations

    for num, i in enumerate(citations):
          if num+1 > i:
                return num
          # print('논문의 개수: {}, 논문 인용 수 {}'.format(num+1, i))
    return len(citations)