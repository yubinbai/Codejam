'''
Created on 2013-6-6

@author: Yubin Bai
'''
import time


class UnionFind:

    def __init__(self, data):
        self.data = data
        self.p = None

    def find(self):
        p = self
        while p.p != None:
            p = p.p
        return p.data

    def union(self, other):
        otherP = other
        rank1 = 0
        while otherP.p != None:
            otherP = otherP.p
            rank1 += 1
        selfP = self
        rank2 = 0
        while selfP.p != None:
            selfP = selfP.p
            rank2 += 1
        if rank2 > rank1:
            selfP.p = otherP
        else:
            otherP.p = selfP


def solve(A, B, P):
    # find the prime numbers
    primes = getPrimes(1000000)
    # make disjoint set
    allSets = {}
    for i in range(A, B + 1):
        allSets[i] = UnionFind(i)
    # sieve to get all sets
    for p in primes:
        if p >= P and p < (B - A + 1):
            firstSet, firstI = None, -1
            for i in range(A, B + 1):
                if i % p == 0:
                    firstSet = allSets[i]
                    firstI = i
                    break
            for i in range(firstI + p, B + 1, p):
                if firstSet.find() != allSets[i].find():
                    firstSet.union(allSets[i])
    uniqueSets = set()
    for i in range(A, B + 1):
        uniqueSets.add(allSets[i].find())
    return '%d' % len(uniqueSets)


def getPrimes(N):
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    results = []
    for i in range(2, N):
        if sieve[i] == True:
            results.append(i)
            for j in range(i * 2, N, i):
                sieve[j] = False
    return results


if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())

    millis1 = int(round(time.time() * 1000))

    for test in range(numOfTests):
        A, B, P = map(int, fIn.readline().strip().split())
        result = solve(A, B, P)
        fOut.write("Case #%d: %s \n" % (test + 1, result))

    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
