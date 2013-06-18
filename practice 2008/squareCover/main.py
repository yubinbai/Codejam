'''
Created on 2013-6-1

@author: Yubin Bai
'''
import time
infinity = 1 << 15

def solve(n, k, points):
    combinations = []
    generate(n, k, combinations)
    
    # memoize the distance
    d = {}
    for i in range(n):
        for j in range(i):
            d[(j, i)] = max(abs(points[i][0] - points[j][0]), \
                           abs(points[i][1] - points[j][1]))
    currMin = infinity
    for c in combinations:
        newMin = _validate(c, d, currMin)
        currMin = min(newMin, currMin)
    return currMin

def generate(n, k, combinations):
    sepPos = []
    _generate(n, k, sepPos, combinations)
    
def _generate(n, k, sepPos, combinations):
    if k - 1 == len(sepPos):
        c = []
        prev = 0
        for i in sepPos:
            curr = []
            for j in range(prev, i):
                curr.append(j)
            prev = i
            c.append(curr)
        curr = []
        for j in range(prev, n):
            curr.append(j)
        c.append(curr)
        combinations.append(c)
        return
    start = 0
    if len(sepPos) > 0:
        start = sepPos[-1]
    for i in range(start + 1, n):
        sepPos.append(i)
        _generate(n, k, sepPos, combinations)
        sepPos.pop()
    
def _validate(c, d, currMin):
    maxD = 0
    for group in c:
        for i in group:
            for j in group:
                if j < i:
                    maxD = max(maxD, d[(j, i)])
                    if maxD >= currMin:
                        return currMin
    return maxD 

    
if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        N, K = [int(x) for x in fIn.readline().strip().split()]
        points = []
        for i in range(N):
            points.append([int(x) for x in fIn.readline().strip().split()])
        result = solve(N, K, points)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
