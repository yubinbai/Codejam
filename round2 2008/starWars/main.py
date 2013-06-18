'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
from pulp import *
parallelSolve = False
infinity = 1 << 40

def solve(par):
    N, ships = par
    prob = LpProblem('solve', LpMinimize)
    
    x = LpVariable("x", 0, 1E6)
    y = LpVariable("y", 0, 1E6)
    z = LpVariable("z", 0, 1E6)
    s = LpVariable("s", 0)
    
    prob += s
    
    for ship in ships:
        x0, y0, z0, p0 = ship
        # 000
        prob += (x0 - x + y0 - y + z0 - z) / p0 <= s
        # 001 
        prob += (x0 - x + y0 - y + z - z0) / p0 <= s
        # 010
        prob += (x0 - x + y - y0 + z0 - z) / p0 <= s
        # 011
        prob += (x0 - x + y - y0 + z - z0) / p0 <= s
        # 100
        prob += (x - x0 + y0 - y + z0 - z) / p0 <= s
        # 101
        prob += (x - x0 + y0 - y + z - z0) / p0 <= s
        # 110
        prob += (x - x0 + y - y0 + z0 - z) / p0 <= s
        # 111
        prob += (x - x0 + y - y0 + z - z0) / p0 <= s
    
    COIN().solve(prob)
    
    return '%.6f' % value(prob.objective)
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
        
