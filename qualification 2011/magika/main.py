'''
Created on 2013-6-9

@author: Yubin Bai

'''
import time
from multiprocessing.pool import Pool
from _collections import defaultdict
parallelSolve = False
infinity = 1 << 30

def solve(par):
    C, combine, D, opposite, N, S = par
    comb = {}
    for c in combine:
        x = list(c)[:2]
        comb[tuple(x)] = c[2]
        x.reverse()
        comb[tuple(x)] = c[2]
    oppo = defaultdict(list)
    for o in opposite:
        oppo[o[0]].append(o[1])
        oppo[o[1]].append(o[0])
    
    result = []
    for s in list(S):
        if len(result) > 0 and (result[-1], s) in comb:
            c = result[-1]
            result.pop()
            result.append(comb[(c, s)])
            continue
        
        flag = True
        if s in oppo:
            for x in oppo[s]:
                if x in result:
                    result = []
                    flag = False
                    break
        if flag:
            result.append(s)
            
    return '[' + ', '.join(result) + ']'
            
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            row = self.fIn.readline().strip().split()
            C = int(row[0])
            del row[0]
            combine = row[:C]
            del row[:C]
            D = int(row[0])
            del row[0]
            opposite = row[:D]
            del row[:D]
            N = int(row[0])
            S = row[1]            

            self.input.append((C, combine, D, opposite, N, S)) 
            
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
        
