'''
Created on 2013-6-2

@author: Yubin Bai
based on permutation and count solution by brute force
'''
import time
infinity = 1 << 25
        
def solve(n, k, edges):
    edgeSet = set()
    for e in edges:
        edgeSet.add((e[0] - 1, e[1] - 1))
        edgeSet.add((e[1] - 1, e[0] - 1))

    permutations = getPermutations(n)
    counter = len(permutations)
    for p in permutations:
        if len(p & edgeSet) > 0:
            counter -= 1
    return counter
            
def getPermutations(n):
    permutations = set()
    path = []
    _getPermutation(path, n, permutations)
    return permutations

def _getPermutation(path, n, permutations):
    if n == len(path):
        p = list(path)
        p.append(p[0])
        edgesInP = set()
        for i in range(1, len(p)):
            if p[i - 1] < p[i]:
                edgesInP.add((p[i - 1], p[i]))
            else:
                edgesInP.add((p[i], p[i - 1]))
        permutations.add(frozenset(edgesInP))
        return
    for i in range(n):
        if i not in path:
            path.append(i)
            _getPermutation(path, n, permutations)
            path.pop()
    
if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        N, K = [int(x) for x in fIn.readline().strip().split()]
        edges = []
        for i in range(K):
            edges.append([int(x) for x in fIn.readline().strip().split()])
        result = solve(N, K, edges)
        fOut.write("Case #%d: %d \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
