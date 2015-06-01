'''
Created on 2013-6-6

@author: Yubin Bai
'''
import time


def solve(A, B, P):
    # find the prime numbers
    primes = getPrimes(1000000)
    # make disjoint set
    parent = []
    for i in range(B - A + 1):
        parent.append(i)
    rank = [0] * (B - A + 1)

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        p1 = i
        while parent[p1] != p1:
            p1 = parent[p1]
        p2 = j
        while parent[p2] != p2:
            p2 = parent[p2]
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
