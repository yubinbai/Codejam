'''
Created on 2013-6-6

@author: Yubin Bai
'''
import time
from memoized import memoized

infinity = 1 << 32
    
def solve(names, queries):
    @memoized
    def cost(step, currName):
        if step == len(queries):
            return 0
        currMin = infinity
        if currName != queries[step]:
            currMin = cost(step + 1, currName)
        for name in names:
            if name != currName:
                currMin = min(currMin, cost(step + 1, name) + 1)
        return currMin
    
    for step in range(len(queries) - 1, -1, -1):
        for name in names:
            cost(step, name)
    result = min([cost(0, name) for name in names])
    return '%d' % result

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        S = int(fIn.readline().strip())
        names = []
        for i in range(S):
            names.append(fIn.readline().strip())
        Q = int(fIn.readline().strip())
        queries = []
        for i in range(Q):
            queries.append(fIn.readline().strip())
        result = solve(names, queries)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
