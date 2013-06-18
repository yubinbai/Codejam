'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
parallelSolve = False

def solve(par):
    P, K, L, freq = par
    freq = list(freq)
    freq.sort()
    freq.reverse()
    total = 0
    pos = 0
    times = 1
    while pos < L:
        total += sum(freq[pos:pos + K]) * times
        pos += K
        times += 1
    
    return '%d' % total

class Solver:
    def getInput(self):
        self.input = []
        for test in range(self.numOfTests):
            P, K, L = map(int, self.fIn.readline().strip().split())
            freq = map(int, self.fIn.readline().strip().split())
            self.input.append((P, K, L, freq)) 
            
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
        
