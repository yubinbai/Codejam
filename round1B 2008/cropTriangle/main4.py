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
    
    modCount = [0] * 9
    for p in points:
        modCount[(p[0] % 3) * 3 + p[1] % 3] += 1
        
    counter = 0
    # The first case.
    for i in range(9):
        # We use the formula for n choose 3 so that,
        # we don't use the same point twice or count
        # the same triangle more than once.
        counter += modCount[i] * (modCount[i] - 1)\
                 * (modCount[i] - 2) / 6;
    
    for i in range(9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 9):
                if (i // 3 + j // 3 + k // 3) % 3 == 0 and\
                        (i + j + k) % 3 == 0:
                    counter += modCount[i] * modCount[j] * modCount[k]
                
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
