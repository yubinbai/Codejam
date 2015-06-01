'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
from numpy import *
parallelSolve = True


def solve(par):
    numberStr = par
    number = []
    size = len(numberStr)
    for i in range(size):
        row = []
        for j in range(size + 1):
            if j > i:
                row.append(int(numberStr[i:j]))
            else:
                row.append(0)
        number.append(row)

    memo = empty((size + 1, 210), dtype=int64)
    memo.fill(-1)
    memo[0, 0] = 1
    for j in range(1, 210):
        memo[0, j] = 0

    def combinations(step, x):
        '''
        dp[step][x] := number of ways we get an expression evaluating
          to x (mod 210) if we only consider the first i
          characters of the string. (*)
        '''
        if memo[step, x % 210] != -1:
            return memo[step, x % 210]

        result = 0
        # no sign in front of it
        currNum = number[0][step]
        if currNum % 210 == x:
            result += 1
        for i in range(1, step):
            currNum = number[i][step]
            for sum2 in range(210):
                if (sum2 + currNum) % 210 == x:
                    result += combinations(i, sum2)
                if (sum2 - currNum) % 210 == x:
                    result += combinations(i, sum2)
        memo[step, x % 210] = result
        return result

    total = 0
    for x in range(210):
        if any([x % s == 0 for s in [2, 3, 5, 7]]):
            total += combinations(len(numberStr), x)
    return '%d' % total


class Solver:

    def getInput(self):
        self.input = []
        self.numOfTests = 20
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
