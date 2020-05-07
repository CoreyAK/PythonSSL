#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
    return sum
    # return sum(ar)


if __name__ == '__main__':
    #fptr = open(os.environ['C:\Users\Corey\PycharmProjects\PythonSSL\Python Basic'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
