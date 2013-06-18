'''
Created on 2013-6-6

@author: Yubin Bai
'''
import time
from shapely.geometry import Point
from shapely.geometry.geo import box
infinity = 1 << 32
    
def solve(f, R, t, r, g):
    # make the circle
    outerCircle = Point(0, 0).buffer(R, 1 << 12)
    # make the ring
    innerCircle = Point(0, 0).buffer(R - t - f, 1 << 12)
    # make the bars
    bars = []
    leftMin = -r - (2 * r + g) * (int(R / (2 * r + g)) + 1) 
    left = leftMin
    while left < R:
        bars.append(box(left, -R, left + 2 * r + 2 * f, R))
        left += 2 * r + g
    
    bottom = leftMin
    while bottom < R:
        bars.append(box(-R, bottom, R, bottom + 2 * r + 2 * f))
        bottom += 2 * r + g
        
    # get the union
    union = outerCircle.difference(innerCircle)
    for bar in bars:
        union = union.union(bar)
    # intersection with prev shape
    finalPattern = union.intersection(outerCircle)    
    # calc area ratio
    result = finalPattern.area / outerCircle.area
    return '%.6f' % result

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for test in range(numOfTests):
        f, R, t, r, g = map(float, fIn.readline().strip().split()) 
        result = solve(f, R, t, r, g)
        fOut.write("Case #%d: %s \n" % (test + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
