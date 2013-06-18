'''
Created on 2013-6-1

@author: Yubin Bai
'''
import time

def solve(N):
    A = [[3, 5], [1, 3]]
    A_n = fast_exponentiation(A, N)
    return str((2 * A_n[0][0] + 999) % 1000 + 10000)[-3:]

def matrix_mult(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][k] = (C[i][k] + A[i][j] * B[j][k]) % 1000
    return C

def fast_exponentiation(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        A1 = fast_exponentiation(A, n / 2)
        return matrix_mult(A1, A1)
    else:
        return matrix_mult(A, fast_exponentiation(A, n - 1))
    
if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        N = int(fIn.readline().strip())
        result = solve(N)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
