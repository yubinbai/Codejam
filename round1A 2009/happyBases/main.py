'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
import pickle
parallelSolve = True
infinity = 1 << 30
maxN = 2000
SQUARE = dict([(c, int(c) ** 2) for c in "0123456789"])

def toBase(base, n):
    result = []
    while n != 0:
        result.append(str(n % base))
        n //= base
    result.reverse()
    return int(''.join(result))

def solve(par):
    bases = par
    d = pickle.load(open('memo.dat','r'))
    
    def isHappy(n, base):
        original = n
        s = set()
        while (n > 1) and (n not in s):
            s.add(n)
            n = toBase(base, n)
            n = toBase(10, sum(SQUARE[d] for d in str(n)))
            if n in d[base]:
                return True
            if n < maxN:
                return False
        return n == 1
    
    i = 2
    while True:
        if all([isHappy(i, b) for b in bases]):
            return i
        i += 1
        
class Solver:
    def getInput(self):
        self.input = []
        for test in range(self.numOfTests):
            bases = map(int, self.fIn.readline().strip().split())
            self.input.append((bases)) 
            
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
        
