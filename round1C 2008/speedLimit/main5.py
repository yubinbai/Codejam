'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
from bisect import bisect_left
parallelSolve = True
infinity = 1 << 36
mod = 1000000007


class FenwickTree:

    '''
    // In this implementation, the tree is represented by a list
    // Elements are numbered by 0, 1, ..., n-1.
    // tree[i] is sum of elements with indexes i&(i+1)..i, inclusive.
    // (Note: this is a bit different from what is proposed in Fenwick's article.
    // To see why it makes sense, think about the trailing 1's in binary
    // representation of indexes.)
    '''

    def __init__(self, size):
        self.tree = [0] * size

    def increase(self, i, delta):
        '''
         Increases value of i-th element by ''delta''.
        '''
        while i < len(self.tree):
            self.tree[i] += delta
            self.tree[i] %= mod
            i |= i + 1

    def getsum(self, left, right):
        '''
        Returns sum of elements with indexes left..right, inclusive; (zero-based);
        '''
        return self._sum(right) - self._sum(left - 1)

    def _sum(self, index):
        currSum = 0
        while index >= 0:
            currSum += self.tree[index]
            index &= index + 1
            index -= 1
        return currSum


def solve(par):
    n, m, X, Y, Z, A = par

    speedIndex = []
    speed = []
    for i in range(n):
        speed.append(float(A[i % m]))
        speedIndex.append(float(speed[-1]))
        A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z

    speedIndex.sort()
    i = j = 0
    while True:
        while i < len(speedIndex) and speedIndex[i] == speedIndex[j]:
            i += 1
        if i == len(speedIndex):
            break
        j += 1
        speedIndex[j] = speedIndex[i]

    del speedIndex[j + 1:]

    tree = FenwickTree(len(speedIndex))
    count = [1] * n
    for i in range(n):
        index = bisect_left(speedIndex, speed[i])
        count[i] += tree._sum(index)
        count[i] %= mod
        tree.increase(index + 1, count[i])
    return str(sum(count) % mod)


class Solver:

    def getInput(self):
        self.input = []
        for test in range(self.numOfTests):
            n, m, X, Y, Z = map(int, self.fIn.readline().strip().split())
            A = []
            for i in range(m):
                A.append(int(self.fIn.readline().strip()))
            self.input.append((n, m, X, Y, Z, A))

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
