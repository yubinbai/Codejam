'''
Created on 2013-6-8

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
parallelSolve = True

def solve(par):
    K, n, pos = par
    deck = [0] * (K + 1)
    currPos = 0
    for i in range(1, K + 1):
        skip = i - 1
        while skip > 0:
            if deck[currPos] == 0:
                skip -= 1
            currPos += 1
            if currPos == K:
                currPos = 0
        while deck[currPos] != 0: 
            currPos += 1
            if currPos == K:
                currPos = 0
        deck[currPos] = i
    result = []
    for p in pos:
        result.append(str(deck[p - 1]))
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
        
