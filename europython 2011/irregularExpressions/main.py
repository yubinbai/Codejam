'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
parallelSolve = False
infinity = 1 << 30

def solve(par):
    S = par
    pos = []
    vowels = []
    for i, v in enumerate(S):
        if v in list('aeiou'):
            pos.append(i)
            vowels.append(v)
    S1 = ''.join(vowels)
    for i in range(len(S1) - 2):
        for j in range(i + 3, len(S1) - 1):
            if S1[i:i + 2] == S1[j:j + 2] and \
                    S[pos[i]:pos[i + 1]] == S[pos[j]:pos[j + 1]]:
                return 'Spell!'
    return 'Nothing.'

class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        for test in range(self.numOfTests):
            S = self.fIn.readline().strip()
            
            self.input.append((S)) 
            
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
        
