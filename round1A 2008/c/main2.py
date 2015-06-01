'''
Created on 2013-6-1

@author: Yubin Bai
'''
import time
from decimal import *

def solve(N):
    getcontext().prec = 100
    three = Decimal('3')
    rootFive = Decimal('5').sqrt()
    result = (three + rootFive) ** N 
    # to makeup the zeros
    result = int(result % 1000)
    return str(result + 10000)[-3:]

def coef(a, b, N):
    # get (3a+ rt5 * b) ^ N
    if N == 1:
        return a, b
    if N % 2 == 0:
        a1, b1 = coef(a, b, N // 2)
        return a1 ** 2 + 5 * b1 ** 2, 2 * a1 * b1 
    else:
        a1, b1 = coef(a, b, N // 2)
        a2, b2 = a1 ** 2 + 5 * b1 ** 2, 2 * a1 * b1
        return a * a2 + 5 * b * b2, a * b2 + a2 * b
if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        N = int(fIn.readline().strip())
        result = solve(N)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
