'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
from memoized import memoized
parallelSolve = False
infinity = 1 << 30

def solve(par):
    k, S = par
    dist = []
    for i in range(k):
        row = [0] * k
        dist.append(row)
    
    minResult = infinity
    # fix t-th element at end of permutation
    for t in range(k):
        # construct the distance
        for i in range(k):
            for j in range(k):
                dist[i][j] = 0
                if i == t:
                    for x in range(len(S) // k - 1):
                        if S[x * k + i] != S[x * k + k + j]:
                            dist[i][j] += 1
                else:
                    for x in range(len(S) // k):
                        if S[x * k + i] != S[x * k + j]:
                            dist[i][j] += 1
        @memoized
        def solve(subset, x):
            if subset == (1 << x):
                return dist[x][0]
            currMin = infinity
            newSet = subset & (~(1 << x))
            for y in range(k):
                if newSet & (1 << y) > 0:
                    r = solve(newSet, y) + dist[x][y]
                    currMin = min(currMin, r)
            return currMin
        
        minResult = min(minResult, solve((1 << k) - 1, 0))

    return '%d' % (minResult + 1)

class Solver:
    def getInput(self):
        self.input = []
        for test in range(self.numOfTests):
            k = int(self.fIn.readline().strip())
            S = self.fIn.readline().strip()
            self.input.append((k, S)) 
            
    def __init__(self):
        self.fIn = open('input.txt')
        self.fOut = open('output.txt', 'w')
        self.numOfTests = int(self.fIn.readline().strip())
        self.results = []
        
    def parallel(self):
        self.getInput()
        p = Pool(4)
        millis1 = int(round(time.time() * 1000))
        self.results = p.map(solve, self.input)
        millis2 = int(round(time.time() * 1000))
        print("Time in milliseconds: %d " % (millis2 - millis1))
        self.makeOutput()

    def sequential(self):
        self.getInput()
        millis1 = int(round(time.time() * 1000))
        for i in self.input:
            self.results.append(solve(i))
        millis2 = int(round(time.time() * 1000))
        print("Time in milliseconds: %d " % (millis2 - millis1))
        self.makeOutput()

    def makeOutput(self):
        for test in range(self.numOfTests):
            self.fOut.write("Case #%d: %s\n" % (test + 1, self.results[test]))
        self.fIn.close()
        self.fOut.close()
    
if __name__ == '__main__':
    solver = Solver()
    if parallelSolve:
        solver.parallel()
    else:
        solver.sequential()
        
