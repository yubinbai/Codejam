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
    s, t = par

    @memoized
    def count(p1, p2):
        if p1 > p2:
            return 0
        if p1 == 0:
            c = 0
            for p in range(p2 + 1):
                if s[p1] == t[p]:
                    c += 1
            return c
        
        currSum = 0
        for p in range(p2 + 1):
            if s[p1] == t[p]:
                currSum += count(p1 - 1, p - 1)
            currSum %= 10000
        return currSum
    
    return str(10000 + count(len(s) - 1, len(t) - 1))[-4:]
    
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            s = "welcome to code jam"
            t = self.fIn.readline().strip()
            self.input.append((s, t))
            
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
        
