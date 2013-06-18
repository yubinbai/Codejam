'''
Created on 2013-6-1

@author: Yubin Bai
based on a graph contraction understanding
!!! not working
'''
import time
infinity = 1 << 25

class Node:    
    def __init__(self, point):
        self.left = self.right = point[0]
        self.top = self.bottom = point[1]
    def merge(self, other):
        self.left = min(self.left, other.left)
        self.right = max(self.right, other.right)
        self.top = max(self.top, other.top)
        self.bottom = min(self.bottom, other.bottom)
    def distance(self, other):
        left = min(self.left, other.left)
        right = max(self.right, other.right)
        top = max(self.top, other.top)
        bottom = min(self.bottom, other.bottom)
        return max(right - left, top - bottom)
def solve(n, k, points):
    nodes = []
    for i in points:
        nodes.append(Node(i))
    result = 0
    while len(nodes) > k:
        minD, minPos1, minPos2 = infinity, -1, -1
        for n1 in range(len(nodes)):
            for n2 in range(n1):
                d = nodes[n1].distance(nodes[n2])
                if minD > d:
                    minD, minPos1, minPos2 = d, n1, n2
        nodes[minPos1].merge(nodes[minPos2])
        del nodes[minPos2]            
        result = max(result, minD)
    return result
    
if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        N, K = [int(x) for x in fIn.readline().strip().split()]
        points = []
        for i in range(N):
            points.append([int(x) for x in fIn.readline().strip().split()])
        result = solve(N, K, points)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
