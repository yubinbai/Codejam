'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
parallelSolve = False
infinity = 1 << 40
def area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    
def solve(par):
    N, M, A = par
    if A > N * M:
        return 'IMPOSSIBLE'
    
    k = A // M
    if k == N:
        x1, y1 = 0, 0 
        x2, y2 = N, 0
        x3, y3 = N, M
    else:
        x1, y1 = 0, A % M
        x2, y2 = k, 0
        x3, y3 = k + 1, M
        
    
    if not A / 2 == area(x1, y1, x2, y2, x3, y3):
        print(False)
    
    return '%d %d %d %d %d %d' % (x1, y1, x2, y2, x3, y3)
    
    
class Solver:
    def getInput(self):
        self.input = []
        for test in range(self.numOfTests):
            N, M, A = map(int, self.fIn.readline().strip().split())
            self.input.append((N, M, A)) 
            
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
        
