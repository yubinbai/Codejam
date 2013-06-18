'''
Created on 2013-6-9

@author: Yubin Bai

'''
import time
from multiprocessing.pool import Pool
parallelSolve = False
infinity = 1 << 30

def solve(par):
    N, keys = par
    orange = []
    blue = []
    cost = 0
    for i, k in enumerate(keys):
        if k[0] == 'O':
            orange.append([i, k[1]])
        else:
            blue.append([i, k[1]])
    currO = currB = 1
    while len(orange) > 0 and len(blue) > 0:
        if orange[0][0] < blue[0][0]:
            stepCost = abs(currO - orange[0][1]) + 1
            currO = orange[0][1]
            del orange[0]
            cost += stepCost
            if blue[0][1] != currB:
                if blue[0][1] > currB:
                    move = min(stepCost, blue[0][1] - currB)
                    currB += move
                else:
                    move = min(stepCost, currB - blue[0][1])
                    currB -= move
        else:
            stepCost = abs(currB - blue[0][1]) + 1
            currB = blue[0][1]
            del blue[0]
            cost += stepCost
            if orange[0][1] != currO:
                if orange[0][1] > currO:
                    move = min(stepCost, orange[0][1] - currO)
                    currO += move
                else:
                    move = min(stepCost, currO - orange[0][1])
                    currO -= move
                    
    while len(orange) > 0:
        stepCost = abs(currO - orange[0][1]) + 1
        currO = orange[0][1]
        del orange[0]
        cost += stepCost
        
    while len(blue) > 0:
        stepCost = abs(currB - blue[0][1]) + 1
        currB = blue[0][1]
        del blue[0]
        cost += stepCost
    
    return cost
            
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            row = self.fIn.readline().strip().split()
            N = int(row[0])
            t = row[1:]
            keys = []
            for i in range(N):
                keys.append([t[i * 2], int(t[i * 2 + 1])])
            self.input.append((N, keys)) 
            
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
        
