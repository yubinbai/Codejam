'''
Created on 2013-6-6

@author: Yubin Bai
'''
import time
from math import sin, sqrt, asin, acos, pi

def circle_segment(rad, th):
    return rad * rad * (th - sin(th)) / 2

def solve(f, R, t, r, g):
    rad = R - t - f
    ar = 0.0
    x1 = r + f
    while x1 < R - t - f:
        y1 = r + f
        while y1 < R - t - f:  
            x2 = x1 + g - 2 * f
            y2 = y1 + g - 2 * f
            if (x2 <= x1 or y2 <= y1):
                y1 += g + 2 * r
                continue
            if (x1 * x1 + y1 * y1 >= rad * rad):
                y1 += g + 2 * r
                continue
            if (x2 * x2 + y2 * y2 <= rad * rad):
                # All points are inside circle.
                ar += (x2 - x1) * (y2 - y1)
            elif (x1 * x1 + y2 * y2 >= rad * rad and x2 * x2 + y1 * y1 >= rad * rad):
                # Only (x1,y1) inside circle.
                ar += circle_segment(rad, acos(x1 / rad) - asin(y1 / rad)) + \
                  (sqrt(rad * rad - x1 * x1) - y1) * \
                  (sqrt(rad * rad - y1 * y1) - x1) / 2
            elif (x1 * x1 + y2 * y2 >= rad * rad):
                # (x1,y1) and (x2,y1) inside circle.
                ar += circle_segment(rad, acos(x1 / rad) - acos(x2 / rad)) + \
                  (x2 - x1) * (sqrt(rad * rad - x1 * x1) - y1 + \
                             sqrt(rad * rad - x2 * x2) - y1) / 2
            elif (x2 * x2 + y1 * y1 >= rad * rad):
                # (x1,y1) and (x1,y2) inside circle.
                ar += circle_segment(rad, asin(y2 / rad) - asin(y1 / rad)) + \
                  (y2 - y1) * (sqrt(rad * rad - y1 * y1) - x1 + \
                             sqrt(rad * rad - y2 * y2) - x1) / 2
            else:
                # All except (x2,y2) inside circle.
                ar += circle_segment(rad, asin(y2 / rad) - acos(x2 / rad)) + \
                  (x2 - x1) * (y2 - y1) - \
                  (y2 - sqrt(rad * rad - x2 * x2)) * \
                  (x2 - sqrt(rad * rad - y2 * y2)) / 2
            y1 += g + 2 * r
        x1 += g + 2 * r
    return '%.6f' % (1.0 - ar / (pi * R * R / 4))

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
