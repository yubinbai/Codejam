'''
Created on 2013-6-9

@author: Yubin Bai
'''
import time
from multiprocessing.pool import Pool
parallelSolve = False
infinity = 1 << 30

def solve(par):
    N, M, mat = par
    
    def dist(y, x, y1, x1, t):
        def light(south):
            if south:
                w0 = t % (mat[y // 2][x // 2][0] + mat[y // 2][x // 2][1])
                if w0 < mat[y // 2][x // 2][0]:
                    w0 = 0
                else:
                    w0 = mat[y // 2][x // 2][0] + mat[y // 2][x // 2][1] - w0
                return 1 + w0
            else:
                w0 = t % (mat[y // 2][x // 2][0] + mat[y // 2][x // 2][1])
                if w0 > mat[y // 2][x // 2][0]:
                    w0 = 0
                else:
                    w0 = mat[y // 2][x // 2][0] - w0
                return 1 + w0
            
        if y1 == y:
            if x % 2 == 1:
                if x1 == x + 1:
                    return 2
                else:
                    return light(south=False)
            else:  # x % 2 == 0
                if x1 == x - 1:
                    return 2
                else:
                    return light(south=False)            
        else:  # x1 == x
            if y % 2 == 1:
                if y1 == y + 1:
                    return 2
                else:
                    return light(south=True)
            else:
                if y1 == y + 1:
                    return light(south=True)
                else:
                    return 2
            return 0

    
    return '%d' % 1
"""
The Bellman-Ford algorithm

Graph API:

    iter(graph) gives all nodes
    iter(graph[u]) gives neighbours of u
    graph[u][v] gives weight of edge (u, v)
"""

# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    d = {}  # Stands for destination
    p = {}  # Stands for predecessor
    for node in graph:
        d[node] = infinity  # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0  # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour] = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph) - 1):  # Run this until is converges
        for u in graph:
            for v in graph[u]:  # For each neighbour of u
                relax(u, v, graph, d, p)  # Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p
        
class Solver:
    def getInput(self):
        self.numOfTests = int(self.fIn.readline().strip())
        self.input = []
        for test in range(self.numOfTests):
            N, M = map(int, self.fIn.readline().strip().split())
            mat = []
            for i in range(N):
                row = map(int, self.fIn.readline().strip().split())
                r = []
                for j in range(M):
                    r.append([row[j * 3:j * 3 + 3]])
                mat.append(r)
            self.input.append((N, M, mat)) 
            
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
        
