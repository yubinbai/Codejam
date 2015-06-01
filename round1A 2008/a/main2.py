'''
Created on 2013-5-29

@author: Yubin Bai
'''

import time
from kuhnMunkres import maxWeightMatching
def minProduct(v1, v2):
    matrix = []
    size = len(v1)
    for i in range(size):
        row = []
        for j in range(size):
            row.append(-v1[i] * v2[j])
        matrix.append(list(row))

    a, b, result = maxWeightMatching(matrix)
    return -result
    
if __name__ == '__main__':
    f = open('input.txt')
    outFile = open('output.txt', 'w')
    numOfTests = int(f.readline())
    
    millis1 = int(round(time.time() * 1000))

    for test in range(numOfTests):
        f.readline()
        v1 = [int(x) for x in f.readline().split()]  # read a line
        v2 = [int(x) for x in f.readline().split()]  # read a line
        result = minProduct(v1, v2)
        outFile.write("Case #%d: %d\n" % (test + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print(millis2 - millis1)
