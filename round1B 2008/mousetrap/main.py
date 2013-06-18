'''
Created on 2013-6-8

@author: Yubin Bai
'''
import time

def solve(K, n, pos):
    deck = [0] * (K + 1)
    currPos = 0
    for i in range(1, K + 1):
        skip = i - 1
        while skip > 0:
            if deck[currPos] == 0:
                skip -= 1
            currPos += 1
            if currPos == K:
                currPos = 0
        while deck[currPos] != 0: 
            currPos += 1
            if currPos == K:
                currPos = 0
        deck[currPos] = i
    result = []
    for p in pos:
        result.append(str(deck[p - 1]))
    return ' '.join(result)
    
if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for test in range(numOfTests):
        K = int(fIn.readline().strip())
        data = map(int, fIn.readline().strip().split())
        n = data[0]
        pos = data[1:] 
        result = solve(K, n, pos)
        fOut.write("Case #%d: %s \n" % (test + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
