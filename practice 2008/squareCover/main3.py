'''
Created on 2013-6-1

@author: Yubin Bai
based on binary search

Now let's write a function that checks if given length is enough to cover n
points with k squares. First, sort all points (top-bottom, left-right).
Then we can use recursion:
[parameters: 
        left - number of squares left
        cover[] - which points have been covered already
]
0. If every point is covered return 1, if left = 0 return 0
1. Out of all free (not covered) points pick top one as UP
2. For each free point as LEFT
        1. If UP and LEFT can't be covered with same square -> continue
        2. Copy cover[] to newcover[]
        3. Mark all points that are covered by square(UP, LEFT) with given 
length
in newcover[]
        4. Run same function with parameters (left-1, newcover[])
        5. Return 1 if (4) returned 1
3. Return 0
'''
import time
infinity = 1 << 25

class Point:    
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]
    def distance(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y))
    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y
class Square:
    def __init__(self, point, size):
        self.x = point.x
        self.y = point.y
        self.size = size
    def hasPoint(self, point):
        if point.x <= self.size + self.x and point.x >= self.x and \
            point.y <= self.size + self.y and point.y >= self.y:
            return True
        else:
            return False
        
def solve(n, k, points):
    p = []
    for i in points:
        p.append(Point(i))
    p.sort()
    low, high = 1, 64001
    while low < high:
        mid = (low + high) // 2
        if check(k, mid, p):
            high = mid
        else:
            low = mid + 1
    return high

def check(k, size, points):
    ptSet = set()
    squares = []
    return _check(k, size, points, ptSet, squares)
    
def _check(k, size, points, ptSet, squares):
    if len(ptSet) == len(points):
        return 1
    if k == 0:
        return 0
    
    pos, bottom = None, infinity
    for p in points:
        if p not in ptSet:
            if bottom > p.y:
                pos, bottom = p, p.y
    for p in points:
        if p not in ptSet and p.distance(pos) <= size:
            squares.append(Square(Point([p.x, pos.y]), size))
            lastSquare = squares[-1]
            changedP = []
            for p in points:
                if lastSquare.hasPoint(p) and p not in ptSet:
                    ptSet.add(p)
                    changedP.append(p)
            if _check(k-1, size, points, ptSet, squares):
                return True
            for p in changedP:
                ptSet.remove(p)
            
    return False
        
    
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
