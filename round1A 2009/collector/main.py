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
    C, N = par
    
    @memoized
    def comb(n, k):
        if n == 0 and k > 0: return 0
        if k == 0 and n >= 0: return 1
        return comb(n - 1, k - 1) + comb(n - 1, k)
    
    def T(x, y):
        res = 1.0 * comb(C - x, y - x) * comb(x, N - (y - x)) / comb(C, N)
        return res
    
    @memoized
    def cost(x):
        if x == C: return 0
        currSum = 1
        r = min(C, x + N)
        for y in range(x + 1, r + 1):
            currSum += T(x, y) * cost(y)
        return currSum / (1 - T(x, x))    
    
    return '%.6f' % cost(0)
    
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            C, N = map(int, self.fIn.readline().strip().split())
            self.input.append((C, N))
            
    def __init__(self):
        self.fIn = open('input.txt')
        self.fOut = open('output.txt', 'w')
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
        
