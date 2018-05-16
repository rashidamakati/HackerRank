import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    pos=0
    neg=0
    z=0
    for x in arr:
        if x>0:
            pos+=1
        elif x<0:
            neg+=1
        elif x==0:
            z+=1

    n=len(arr)
    print(pos/n)
    print(neg/n)
    print(z/n)
    #

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
