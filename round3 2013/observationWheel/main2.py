'''
Created on Jun 29, 2013

@author: Yubin Bai

All rights reserved.
'''

import time
from multiprocessing.pool import Pool
parallelSolve = False
INF = 1 << 30


def solve(par):
    status = par
    N = len(status)
    memo = [-1.0] * (1 << N)
    memo[-1] = 0.0

    def avg(w):
        if memo[w] != -1.0:
            return memo[w]
        s = 0.0
        for i in range(N):
            j = i
            r = N
            while True:
                if not ((1 << j) & w):
                    s += r
                    s += avg((1 << j) | w)
                    break
                else:
                    r -= 1
                    j += 1
                    j %= N
        currAvg = 1.0 * s / N
        memo[w] = currAvg
        return currAvg

    n = int(status.replace('.', '0').replace('X', '1'), base=2)
    return '%.10f' % avg(n)


class Solver:

    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            row = self.fIn.readline().strip()
            self.input.append(row)

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
