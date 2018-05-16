import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    n=len(a)
    d1=0
    d2=0
    x=0
    for fir in a:
        d1+=fir[x]
        x+=1
    for sec in a:
        d2+=sec[n-1]
        n-=1

    return abs(d1-d2)


    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
