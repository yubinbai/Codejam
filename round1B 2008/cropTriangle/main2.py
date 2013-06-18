'''
Created on 2013-6-6

@author: Yubin Bai
'''
import time

def solve(n, A, B, C, D, x0, y0, M):
    points = []
    X = x0; Y = y0
    points.append([X, Y])
    for i in range(n - 1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        points.append([X, Y])

    counter = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            xTarget = (3 - points[i][0] - points[j][0]) % 3
            yTarget = (3 - points[i][1] % 3 - points[j][1]) % 3
            for k in range(j + 1, n):
                if xTarget == points[k][0] % 3 and yTarget == points[k][1] % 3:
                    counter += 1
                
    return '%d' % counter
    

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for test in range(numOfTests):
        n, A, B, C, D, x0, y0, M = map(int, fIn.readline().strip().split()) 
        result = solve(n, A, B, C, D, x0, y0, M)
        
        fOut.write("Case #%d: %s \n" % (test + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
