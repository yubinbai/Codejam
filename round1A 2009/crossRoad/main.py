'''
Created on 2013-6-9

@author: Yubin Bai

DP cannot work because the choice of four directions will lead to deadlock
'''
import time
from multiprocessing.pool import Pool
from memoized import memoized
parallelSolve = False
infinity = 1 << 30

def solve(par):
    N, M, mat = par
    
    def dist(y, x, y1, x1, t):
        def light(south):
            if south:
                w0 = t % (mat[y // 2][x // 2][0] + mat[y // 2][x // 2][1])
                if w0 < mat[y // 2][x // 2][0]:
                    w0 = 0
                else:
                    w0 = mat[y // 2][x // 2][0] + mat[y // 2][x // 2][1] - w0
                return 1 + w0
            else:
                w0 = t % (mat[y // 2][x // 2][0] + mat[y // 2][x // 2][1])
                if w0 > mat[y // 2][x // 2][0]:
                    w0 = 0
                else:
                    w0 = mat[y // 2][x // 2][0] - w0
                return 1 + w0
            
        if y1 == y:
            if x % 2 == 1:
                if x1 == x + 1:
                    return 2
                else:
                    return light(south=False)
            else:  # x % 2 == 0
                if x1 == x - 1:
                    return 2
                else:
                    return light(south=False)            
        else:  # x1 == x
            if y % 2 == 1:
                if y1 == y + 1:
                    return 2
                else:
                    return light(south=True)
            else:
                if y1 == y + 1:
                    return light(south=True)
                else:
                    return 2
            return 0
    
    @memoized
    def cost(y, x):
        if y == 0 and x == 2 * M - 1:
            return 0
        currMin = infinity
        for y1, x1 in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
            if y1 >= 0 and y1 <= 2 * N - 1 and x1 >= 0 and x1 <= 2 * M - 1:
                t = cost(y1, x1)
                currMin = min(currMin, t + dist(y, x, y1, x1, t))
        return currMin
    
    return '%d' % cost(2 * N - 1, 0)

        
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            N, M = map(int, self.fIn.readline().strip().split())
            mat = []
            for i in range(N):
                row = map(int, self.fIn.readline().strip().split())
                r = []
                for j in range(M):
                    r.append([row[j * 3:j * 3 + 3]])
                mat.append(r)
            self.input.append((N, M, mat)) 
            
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
        
