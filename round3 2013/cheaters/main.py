'''
Created on Jun 18, 2013

@author: Yubin Bai

All rights reserved.
'''

import time
from multiprocessing.pool import Pool
import itertools
parallelSolve = False
infinity = 1 << 30

def solve(par):
    B, N, bets = par
    heights = list(bets)
    heights.extend([0] * (37 - len(bets)))
    heights.sort()
    
    def p(pos):
        '''
        find the profit of each vertical position
        '''
        def cost(h):
            '''
            cost of building a step of h
            '''
            currB = B
            for i, v in enumerate(heights):
                if i < pos and v < h:
                    currB -= (h - v)
                if i >= pos and v < h + 1:
                    currB -= (h + 1 - v)
                if currB < 0:
                    return infinity
            return B - currB
                        
        left = 0
        right = (B + sum(heights)) // 37 + 1
        while left < right - 1:
            mid = (left + right) // 2
            if cost(mid) == infinity:
                right = mid - 1
            else:
                left = mid
        counter = len(list(itertools.ifilter(lambda e: e < left, heights)))
        counter = min(counter, pos)
        c = cost(left)
        profit = 1.0 * counter / pos * left * 36 - c
        return max(0.0, profit)
 
    profit = max(map(p, range(1, 37)))
    return '%.10f' % profit
        
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            B, N = map(int, self.fIn.readline().strip().split())
            bets = map(int, self.fIn.readline().strip().split())
            self.input.append((B, N, bets)) 
            
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
        
