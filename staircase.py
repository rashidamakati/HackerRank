
import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    #
    z=n-1

    for x in range(n):
        print(' '*(z)+'#'*(x+1))
        z-=1


    #

if __name__ == '__main__':
    n = int(input())

    staircase(n)
