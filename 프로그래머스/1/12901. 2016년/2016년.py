from datetime import datetime
weekday = {6:'SUN', 0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT'}
def solution(a, b):
    date = '2016-{}-{}'.format(a, b)
    date = datetime.strptime(date, '%Y-%m-%d')
    answer = weekday[date.weekday()]
    return answer