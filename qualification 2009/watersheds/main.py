'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
from memoized import memoized
parallelSolve = True
infinity = 1 << 30

def solve(par):
    H, W, m = par
    
    def isSink(y, x):
        for y2, x2 in [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]:
            if y2 >= 0 and y2 < H and x2 >= 0 and x2 < W and m[y2][x2] < m[y][x]:
                return False
        return True
    
    @memoized
    def findSink(y, x):
        if isSink(y, x):
            return y, x
        
        minY, minX, currMin = -1, -1, infinity
        for y1, x1 in [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]:
            if y1 >= 0 and y1 < H and x1 >= 0 and x1 < W and m[y1][x1] < currMin:
                minY, minX, currMin = y1, x1, m[y1][x1]
                
        if isSink(minY, minX):
            return minY, minX
        else:
            return findSink(minY, minX)
    
    label = []
    for i in range(H):
        label.append([None] * W)

    currLabel = 0
    labelList = list('abcdefghijklmnopqrstuvwxyz')  
    for y in range(H):
        for x in range(W):
            if label[y][x] != None:
                continue
            y1, x1 = findSink(y, x)
            if label[y1][x1] == None:
                label[y][x] = labelList[currLabel]
                label[y1][x1] = labelList[currLabel]
                currLabel += 1
            else:
                label[y][x] = label[y1][x1]
    result = []
    for row in label:
        result.append('\n')
        result.append(' '.join(row))
    return ''.join(result)
    
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            H, W = map(int, self.fIn.readline().strip().split())
            m = []
            for i in range(H):
                m.append(map(int, self.fIn.readline().strip().split()))
            self.input.append((H, W, m))
            
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
        
