'''
Created on 2013-6-9

@author: Yubin Bai

'''
import time
from multiprocessing.pool import Pool
from collections import deque
parallelSolve = False
infinity = 1 << 30

maxN = 2000000
memo = [None] * (maxN + 1)

def makeMemo():
    global memo
    for i in range(maxN + 1):
        if memo[i] == None:
            l = []
            memo[i] = l
            s = str(i)
            q = deque(s)
            for j in range(len(q)):
                q.rotate(1)
                s1 = ''.join(q)
                s2 = s1.lstrip('0')
                if s1 == s2 and int(s1) <= maxN:
                    if int(s1) not in l:
                        l.append(int(s1))
                        memo[int(s1)] = l
            l.sort()

def solve(par):
    A, B = par
    counter = 0
    for i in range(A + 1, B + 1):
        for j in memo[i]:
            if j >= i:
                break
            if j >= A:
                counter += 1
    return counter
    
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            A, B = map(int, self.fIn.readline().strip().split())
            self.input.append((A, B)) 
            
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
    makeMemo()
    solver = Solver()
    if parallelSolve:
        solver.parallel()
    else:
        solver.sequential()
        
