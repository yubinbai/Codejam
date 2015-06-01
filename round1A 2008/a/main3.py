'''
Created on 2013-5-30

@author: Yubin Bai
'''
import time
def minProduct(v1, v2):
    v1.sort()
    v2.sort()
    v2.reverse()
    total = 0
    size = len(v1)
    for i in range(size):
        total += v1[i] * v2[i]
    return total 

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