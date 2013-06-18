'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
parallelSolve = True

def solve(par):
    K, n, queries = par
    answers = [-1] * n
    pos = 0
    for i in range(1, K + 1):
        # Compute the next position, after wrap-around.
        pos = (pos + i - 1) % (K - i + 1);
        for j in range(n):
            if answers[j] < 0:
                if queries[j] == pos + 1:
                    queries[j] = -1
                    answers[j] = i
                elif queries[j] > pos + 1:
                    # The effect of deleting the next position.
                    queries[j] -= 1
    result = []
    for p in answers:
        result.append(str(p))
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
        
