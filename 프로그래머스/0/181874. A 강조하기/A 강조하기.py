def solution(myString):
    for i in myString:
      if i != 'a' and i != 'A': 
        myString = myString.replace(i, i.lower())
      else: myString = myString.replace(i, i.upper())
    return myString