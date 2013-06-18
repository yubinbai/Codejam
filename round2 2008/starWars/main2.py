'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
parallelSolve = True
infinity = 1 << 40

def solve(par):
    N, ships = par
    
    def solve(x0, y0, z0, N):
        result = 0.0
        for i in range(N): 
            d = (abs(x0 - ships[i][0]) + abs(y0 - ships[i][1])\
                         + abs(z0 - ships[i][2])) / ships[i][3]
            result = max(result, d)
        return result

    x0 = y0 = z0 = 0.0
    L = 1E6
    r0 = solve(x0, y0, z0, N)
    for step in range(1000):
        temp = 0.0
        temp = solve(x0 - L, y0, z0, N)
        if temp < r0:
            r0 = temp
            x0 -= L
        temp = solve(x0 + L, y0, z0, N)
        if temp < r0:
            r0 = temp
            x0 += L
        temp = solve(x0, y0 - L, z0, N)
        if temp < r0:
            r0 = temp
            y0 -= L
        temp = solve(x0, y0 + L, z0, N)
        if temp < r0:
            r0 = temp
            y0 += L
        temp = solve(x0, y0, z0 - L, N)
        if temp < r0:
            r0 = temp
            z0 -= L
        temp = solve(x0, y0, z0 + L, N)
        if temp < r0:
            r0 = temp
            z0 += L
        if (step + 1) % 6 == 0:
            L /= 1.618
    
    return '%.7f' % r0
class Solver:
    def getInput(self):
        self.input = []
        for test in range(self.numOfTests):
            N = int(self.fIn.readline().strip())
            ships = []
            for i in range(N):
                ships.append(map(float, self.fIn.readline().strip().split()))
            self.input.append((N, ships)) 
            
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
        
