'''
Created on 2013-6-8

@author: Yubin Bai
'''
import time

def solve(K, n, queries):
    answers = [-1] * n
    pos = 0
    for i in range(1, K + 1):
        # Compute the next position, after wrap-around.
        pos = (pos + i - 1) % (K - i + 1);
        for j in range(n):
            if answers[j] < 0:
                if queries[j] == pos + 1:
                    queries[j] = -1
                    answers[j] = i
                elif queries[j] > pos + 1:
                    # The effect of deleting the next position.
                    queries[j] -= 1
    result = []
    for p in answers:
        result.append(str(p))
    return ' '.join(result)
    
if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for test in range(numOfTests):
        K = int(fIn.readline().strip())
        data = map(int, fIn.readline().strip().split())
        n = data[0]
        pos = data[1:] 
        result = solve(K, n, pos)
        fOut.write("Case #%d: %s \n" % (test + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
