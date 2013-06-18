'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
parallelSolve = False
infinity = 1 << 30

def solve(par):
    N, songs = par
    
    def find(s, songs):
        for i in range(len(s) + 1):
            ans = []
            for j in range(len(s) - i + 1):
                sub = s[j:j + i].lower()
                if not any(sub in s for s in songs):
                    ans.append(str(sub))
            if ans:
                ans = [a.upper() for a in ans]
                ans.sort()
                return '"%s"' % ans[0]
        return ':('
    
    results = []
    for s in songs:
        songs1 = [z.lower() for z in songs]
        songs1.remove(s.lower())
        results.append(find(s, songs1))
    return '\n' + '\n'.join(results)


class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        for test in range(self.numOfTests):
            N = int(self.fIn.readline().strip())
            songs = []
            for i in range(N):
                songs.append(self.fIn.readline().strip())
            
            self.input.append((N, songs)) 
            
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
        
