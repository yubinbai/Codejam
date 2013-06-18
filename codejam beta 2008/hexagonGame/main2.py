'''
Created on 2013-6-4

@author: Yubin Bai
'''
import time
from kuhnMunkres import maxWeightMatching
import collections

infinity = 1 << 32

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = -x - y
    def distance(self, other):
        return max(abs(self.x - other.x), \
                   abs(self.y - other.y), abs(self.z - other.z))
    def __lt__(self, other):
        if self.y != other.y:
            return self.y < other.y
        else:
            return self.x > other.x

def solve(S, pos, weight):
    coordinates = set()
    frontier = collections.deque()
    frontier.append((0, 0))
    coordinates.add((0, 0))
    for i in range((S - 1) // 2):
        length = len(frontier)
        for j in range(length):
            x, y = frontier.popleft()
            for x1, y1 in [(x + 1, y), (x + 1, y - 1), (x, y - 1), \
                           (x - 1, y), (x - 1, y + 1), (x, y + 1)]:
                if (x1, y1) not in coordinates:
                    frontier.append((x1, y1))
                    coordinates.add((x1, y1))
    cells = []
    for c in coordinates:
        cells.append(Cell(c[0], c[1]))
    cells.sort()
    
    def findMatch():    
        distance = []  # use negative distance
        for i in range(S):
            row = []
            for j in range(S):
                d = cells[pos[i] - 1].distance(target[j])
                v = -1 * weight[i] * d
                row.append(v)
            distance.append(row)

        v = maxWeightMatching(distance)[2]
        return -1.0 * v
    
    target = []
    for c in cells:
        if c.x == 0:
            target.append(c)
    result1 = findMatch()
    
    target = []
    for c in cells:
        if c.y == 0:
            target.append(c)
    result2 = findMatch()    
    
    target = []
    for c in cells:
        if c.z == 0:
            target.append(c)
    result3 = findMatch()
    
    return str(int(min(result1, result2, result3)))

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        pos = [int(x) for x in fIn.readline().strip().split()]
        weight = [int(x) for x in fIn.readline().strip().split()]
        S = len(pos)
        
        result = solve(S, pos, weight)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
