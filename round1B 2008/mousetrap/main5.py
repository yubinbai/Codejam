'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
from fenwick import FenwickTree
parallelSolve = False

def solve(par):
    K, n, queries = par
    circle = [None] * K
    tree = FenwickTree(K)
    for i in range(K):
        tree.increase(i, 1)
    
    pos = 0
    for i in range(K):
        # Compute the next position, after wrap-around.
        space = tree.getsum(0, K - 1)
        target = i + 1
        if target % space == 0:
            target = space
        else:
            target %= space
        left = pos
        right = left - 1 + K
        while left < right:
            mid = (left + right) // 2
            count = tree.getsum(pos, mid % K)
            if count == target and circle[mid % K] == None:
                circle[mid % K] = i + 1
                pos = (mid + 1) % K
                tree.increase(mid % K, -1)
                break
            elif count < target:
                left = mid 
            else:
                right = mid

    result = []
    for q in queries:
        result.append(str(circle[q - 1]))
    return ' '.join(result)

class Solver:
    def __init__(self):
        self.fIn = open('input.txt')
        self.fOut = open('output.txt', 'w')
        self.numOfTests = int(self.fIn.readline().strip())
        self.results = []
        
    def getInput(self):
        self.input = []
        for test in range(self.numOfTests):
            K = int(self.fIn.readline().strip())
            data = map(int, self.fIn.readline().strip().split())
            n = data[0]
            pos = data[1:]
            self.input.append((K, n, pos)) 
        
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
        
