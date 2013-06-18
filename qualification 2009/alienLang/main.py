'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
import re
from multiprocessing.pool import Pool
parallelSolve = False
infinity = 1 << 30

def solve(par):
    p, words = par
    e = re.compile(p.replace('(', '[').replace(')', ']'))
    counter = 0
    for w in words:
        if e.match(w) != None:
            counter += 1
    return '%d' % counter

class Solver:
    def getInput(self):
        L, D, self.numOfTests = map(int, self.fIn.readline().strip().split())
        words = []
        for i in range(D):
            words.append(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            p = self.fIn.readline().strip()
            self.input.append((p, words)) 
            
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
        
