'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
from memoized import memoized
parallelSolve = False
infinity = 1 << 40

def solve(par):
    M, V, tree = par
    @memoized
    def minChange(root, value):
        if root >= len(tree):
            return infinity
        
        if len(tree[root]) == 2:  # gate
            left0 = minChange(root * 2 + 1, 0)
            left1 = minChange(root * 2 + 1, 1)
            right0 = minChange(root * 2 + 2, 0)
            right1 = minChange(root * 2 + 2, 1)

            if tree[root][1]:  # changeable
                if tree[root][0]:  # and 
                    if value:
                        return min(left1 + right1, 1 + left0 + right1, 1 + left1 + right0)
                    else:
                        return min(left1 + right0, left0 + right1, left0 + right0)
                else:  # or
                    if value:
                        return min(left0 + right1, left1 + right0, left1 + right1)
                    else:
                        return min(left0 + right0, 1 + left0 + right1, 1 + left1 + right0)
            else:  # cannot change
                if tree[root][0]:  # and
                    if value:
                        return left1 + right1
                    else:
                        return min(left0 + right1, left1 + right0, left0 + right0)
                else:  # or
                    if value:
                        return min(left0 + right1, left1 + right0, left1 + right1)
                    else:
                        return left0 + right0
        else:  # leaf
            if tree[root][0] == value:
                return 0
            else:
                return infinity
            
    result = minChange(0, V)
    if result >= infinity:
        return 'IMPOSSIBLE'
    else:
        return '%d' % result 
    
class Solver:
    def getInput(self):
        self.input = []
        for test in range(self.numOfTests):
            M, V = map(int, self.fIn.readline().strip().split())
            nodes = []
            for i in range(M):
                nodes.append(map(int, self.fIn.readline().strip().split()))
            self.input.append((M, V, nodes)) 
            
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
        
