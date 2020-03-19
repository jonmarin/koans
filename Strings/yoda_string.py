
from sys import stdin, stdout
import typing


def reverse( str, first, last):
    strlist = list( str )
    while first < last :
        strlist[first], strlist[last] = strlist[last], strlist[first]
        first += 1
        last -= 1

    return strlist

def yoda_string( str ):
    if str == None:
        return ""
    elif len(str) == 0:
        return ""
    else:
        reversed = str[::-1]
        current = 0
        for i in range(len(reversed)):
            if reversed[i] == ' ':
                reverse( reversed, current, i-1)
                current = i

        print(reversed)



print("Enter a sentence:")
ret = yoda_string( stdin.readline() )
