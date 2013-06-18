'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
from _collections import defaultdict, deque
parallelSolve = False
infinity = 1 << 30

def solve(par):
    N, F = par
    follow = defaultdict(set)
    for i, f in enumerate(F):
        follow[f].add(i + 1)
    
    results = []
    for day in range(1, N + 1):
        notified = set()
        frontier = deque([day])
        while len(frontier) > 0:
            curr = frontier.popleft()
            if curr in notified:
                continue
            notified.add(curr)
            for m in follow[curr]:
                frontier.append(m)
        results.append(str(len(notified)))
    
    return '\n' + '\n'.join(results)
    
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        for test in range(self.numOfTests):
            N = int(self.fIn.readline().strip())
            F = map(int, self.fIn.readline().strip().split())
            
            self.input.append((N, F)) 
            
    def __init__(self):
        self.fIn = open('input.txt')
        self.fOut = open('output.txt', 'w')
        self.input = []
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
        
