MULTIPLE_3_TXT = "Fooz"
MULTIPLE_5_TXT = "Buzz"

def fizzBuzz(num):    
    arr = []
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append(MULTIPLE_3_TXT + MULTIPLE_5_TXT)
        elif i % 3 == 0:
            arr.append(MULTIPLE_3_TXT)
        elif i % 5 == 0:
            arr.append(MULTIPLE_5_TXT)
        else:
            arr.append(i)
    return arr
