'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
from bintrees.rbtree import RBTree
parallelSolve = True
infinity = 1 << 36

def solve(par):
    n, m, X, Y, Z, A = par
    speed = []
    for i in range(n):
        speed.append(A[i % m])
        A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z

    sumCount = RBTree()
    count = [1] * (n)
    
    for i in range(n):
        try:
            sumCount[speed[i]] += 0
        except KeyError:
            sumCount[speed[i]] = 0

        s = speed[i]
        while True:
            try:
                s, v = sumCount.prev_item(s)
                count[i] += v
            except KeyError:
                break
        sumCount[speed[i]] += count[i]
        
    return str(sum(count))

class Solver:
    def getInput(self):
        self.input = []
        for test in range(self.numOfTests):
            n, m, X, Y, Z = map(int, self.fIn.readline().strip().split())
            A = []
            for i in range(m):
                A.append(int(self.fIn.readline().strip()))
            self.input.append((n, m, X, Y, Z, A)) 
            
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
        
