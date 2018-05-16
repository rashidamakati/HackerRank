#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if "PM" in s:
        newfortmat = s[:-2]
        numtime = newfortmat.split(":")
        convt = int(numtime[0])
        if convt==12:
            convt=12
        else:
            convt+=12

        numtime[0] = str(convt)
        newfort = ':'.join(numtime)
        return(newfort)
    else:
        newf = s[:-2]
        numtime = newf.split(":")
        convt = int(numtime[0])
        if convt==12:
            numtime[0] = "00"

        newfort = ':'.join(numtime)
        return(newfort)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
