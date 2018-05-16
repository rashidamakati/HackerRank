import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    #

    i=min(arr)
    j=max(arr)
    sum = 0

    for n in arr:
        sum +=n


    minnum=sum-j
    maxnum=sum-i
    print(minnum,maxnum)




    #

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
