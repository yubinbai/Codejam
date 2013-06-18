'''
Created on 2013-6-1

@author: Yubin Bai
'''
import time

def solve(white, black):
    if black % 2 == 0:
        return 'WHITE'
    else:
        return 'BLACK'
if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        white, black = [int(x) for x in fIn.readline().strip().split()]
        result = solve(white, black)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
