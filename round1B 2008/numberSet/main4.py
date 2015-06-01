'''
Created on 2013-6-6
@author: Yubin Bai

numpypy is not faster compared to pypy lists in this case
'''
import numpypy
import numpy as np
import time
from multiprocessing.pool import Pool
parallelSolve = True


def solve(par):
    A, B, P, primes = par

    # make disjoint set
    parent = np.array(range(B - A + 1), np.int64)
    for i in range(B - A + 1):
        parent[i] = i
    rank = np.zeros((B - A + 1,), np.int32)

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        p1 = find(i)
        p2 = find(j)
        if rank[p1] < rank[p2]:
            parent[p1] = p2
        else:
            parent[p2] = p1
            if rank[p1] == rank[p2]:
                rank[p1] += 1

    # sieve to get all sets
    result = B - A + 1
    for p in primes:
        if p >= (B - A + 1):
            break
        if p >= P:
            x = (A // p) * p
            if x < A:
                x += p
            x -= A
            for y in range(x, B - A + 1, p):
                if find(x) != find(y):
                    result -= 1
                    union(x, y)

    return '%d' % result


def getPrimes(N):
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, N):
        if sieve[i] == True:
            yield i
            for j in range(i * 2, N, i):
                sieve[j] = False


class Solver:

    def getInput(self):
        self.numOfTests = int(self.fIn.readline())
        self.input = []
        for i in range(self.numOfTests):
            A, B, P = map(int, self.fIn.readline().strip().split())
            self.input.append((A, B, P, self.primes))

    def __init__(self):
        self.fIn = open('input.txt')
        self.fOut = open('output.txt', 'w')
        self.results = []
        self.primes = list(getPrimes(1000000))

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
            self.fOut.write("Case#%d: %s\n" % (test + 1, self.results[test]))
        self.fIn.close()
        self.fOut.close()

if __name__ == '__main__':
    solver = Solver()
    if parallelSolve:
        solver.parallel()
    else:
        solver.sequential()
