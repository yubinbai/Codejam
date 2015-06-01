'''
Created on Jun 18, 2013

@author: Yubin Bai

All rights reserved.
'''

import time
from multiprocessing.pool import Pool
import itertools
parallelSolve = False
INF = 1 << 30

def solve(par):
    N, points = par
    r = list(range(0, N))
    currOrder = []
    currMax = -1
    
    def area(order):
        def det(i, j):
            return points[i][0] * points[j][1] - points[j][0] * points[i][1]
        currSum = 0
        for i, v in enumerate(order):
            if i == N - 1:
                currSum += det(v, order[0])
            else:
                currSum += det(v, order[i + 1])
        return currSum           
            
    for order in itertools.permutations(r):
        a = area(order)
        if a > currMax:
            currMax = a 
            currOrder = list(order)
            
    return ' '.join([str(e) for e in currOrder])
        
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            N = int(self.fIn.readline().strip())
            points = []
            for i in range(N):
                points.append(map(int, self.fIn.readline().strip().split()))
            self.input.append((N, points)) 
            
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
        
