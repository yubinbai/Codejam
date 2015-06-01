'''
Created on Jun 18, 2013

@author: Yubin Bai

All rights reserved.
'''

import time
from multiprocessing.pool import Pool
parallelSolve = True
infinity = 1 << 30


def solve(par):
    N, M, S = par

    P = [list([0] * (N + 2)) for i in range(M)]
    for i, row in enumerate(P):
        if S[i][1] == 'T':
            row[int(S[i][0])] += 1
            row[int(S[i][2])] += 1
            row[N + 1] = 0
        elif S[i][1] == 'L':
            row[int(S[i][0])] += 1
            row[int(S[i][2])] += 1
            row[N + 1] = 1
        elif S[i][1] == 'S':
            row[int(S[i][0])] += 1
            row[int(S[i][2])] += 1
            row[int(S[i][3])] += 1
            row[N + 1] = 1
        elif S[i][1] == 'D':
            row[int(S[i][0])] += 1
            row[int(S[i][2])] += 1
            row[int(S[i][3])] += 1
            row[N + 1] = 0
    for row in P:
        for j, v in enumerate(row):
            row[j] %= 2

    '''
    gauss elimination
    '''
    P.sort()
    P.reverse()
    for i in range(M - 1):
        pos = -1
        for j in range(1, N + 1):
            if P[i][j] != 0:
                pos = j
                break
        if pos == -1:
            continue

        for j in range(i + 1, M):
            if P[j][pos] == 0:
                continue
            for k in range(pos, N + 2):
                P[j][k] -= P[i][k]
                P[j][k] %= 2
        P.sort()
        P.reverse()

    for i in range(M - 1, 0, -1):
        pos = -1
        for j in range(1, N + 1):
            if P[i][j] != 0:
                pos = j
                break
        if pos == -1:
            continue

        for j in range(i - 1, -1, -1):
            if P[j][pos] == 0:
                continue
            for k in range(pos, N + 2):
                P[j][k] -= P[i][k]
                P[j][k] %= 2

    result = [-1] * (N + 1)
    for row in P:
        if sum(row[:-1]) == 1:
            for j in range(1, N + 1):
                if row[j]:
                    result[j] = row[-1]
                    break

    res = {1: 'T', 0: 'L', -1: '-'}
    return ' '.join(res[i] for i in result[1:])


class Solver:

    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            row = map(int, self.fIn.readline().strip().split())
            N, M = row[0], row[1]
            S = []
            for i in range(M):
                S.append(self.fIn.readline().strip().split())
            self.input.append((N, M, S))

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
