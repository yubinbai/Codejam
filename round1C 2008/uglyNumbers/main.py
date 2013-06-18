'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
from memoized import memoized
parallelSolve = True

def solve(par):
    numberStr = par
    number = {}
    size = len(numberStr)
    for i in range(size):
        for j in range(i + 1, size + 1):
            number[(i, j)] = int(numberStr[i:j])
    @memoized
    def combinations(step, x):
        '''        
        dyn[step][x] := number of ways we get an expression evaluating 
          to x (mod 210) if we only consider the first i
          characters of the string. (*)
        '''
        if step == 0:
            if x == 0:
                return 1
            else:
                return 0
        result = 0
        # no sign in front of it
        currNum = number[(0, step)]
        if currNum % 210 == x:
            result += 1
        for i in range(1, step):
            currNum = number[(i, step)]
            for sum2 in range(210):
                if (sum2 + currNum) % 210 == x:
                    result += combinations(i, sum2)
                if (sum2 - currNum) % 210 == x:
                    result += combinations(i, sum2)
        return result
    
    total = 0
    for x in range(210):
        if any([x % s == 0 for s in [2, 3, 5, 7]]):
            total += combinations(len(numberStr), x)
    return '%d' % total
    
class Solver:
    def getInput(self):
        self.input = []
        for test in range(self.numOfTests):
            numberStr = self.fIn.readline().strip()
            self.input.append((numberStr)) 
            
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
            self.fOut.write("Case #%d: %s \n" % (test + 1, self.results[test]))
        self.fIn.close()
        self.fOut.close()
    
if __name__ == '__main__':
    solver = Solver()
    if parallelSolve:
        solver.parallel()
    else:
        solver.sequential()
        
