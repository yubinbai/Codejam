'''
Created on 2013-6-1

@author: Yubin Bai
'''
import time
from bellman import bellman_ford
infinity = 1 << 32

def solve(N, source, edges):
    graph = {}
    vertices = set()
    for e in edges:
        vertices.add(e[0])
        vertices.add(e[1])
        e[2] = int(e[2])
    for v in vertices:
        graph[v] = {}
    for e in edges:
        if e[1] in graph[e[0]]:
            graph[e[0]][e[1]] = min(e[2], graph[e[0]][e[1]])
        else:
            graph[e[0]][e[1]] = e[2]
    
    d, p = bellman_ford(graph, source)
    
    def getPaths(source, target, cost):
        if source == target and cost == 0:
            allPath.append(list(currPath))
            return 
        for i in range(len(edges)):
            if edges[i][0] == source and edges[i][2] <= cost and i not in currPath:
                currPath.append(i)
                getPaths(edges[i][1], target, cost - edges[i][2])
                currPath.pop()    
    
    probabilities = [0] * N
    destCount = 0
    for v in d:
        if d[v] != 0 and d[v] != float('Inf'):
            destCount += 1
            allPath = []
            currPath = []
            getPaths(source, v, d[v])
            for i in range(len(edges)):
                currCount = 0
                for p in allPath:
                    if i in p:
                        currCount += 1
                if len(allPath) > 0:
                    probabilities[i] += currCount * 1.0 / len(allPath)
    
    for i in range(N):
        probabilities[i] /= destCount
    
    return ' '.join([('%.7f' % x) for x in probabilities])


if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        nStr, name = fIn.readline().strip().split()
        N = int(nStr)
        edges = []
        for i in range(N):
            edges.append(fIn.readline().strip().split())
        result = solve(N, name, edges)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
