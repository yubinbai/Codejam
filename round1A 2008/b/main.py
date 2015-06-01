'''
Created on May 30, 2013

@author: Yubin Bai
'''
import time

class Customer:
    def __init__(self, data):
        self.malted = set()
        self.unmalted = set()
        for i in range(0, len(data), 2):
            if data[i + 1] == 0:
                self.unmalted.add(data[i] - 1)
            else:
                self.malted.add(data[i] - 1)
            
def solve(N, M, customers):
    selections = [0] * N
    satisfied = set()
    while len(satisfied) < M:
        satisfied = set()
        for c in customers:
            for i in range(N):
                if selections[i] == 0 and i in c.unmalted \
                        or selections[i] == 1 and i in c.malted:
                    satisfied.add(c)
                    break
        for c in customers:
            if c not in satisfied:
                if len(c.malted) == 0 and \
                        all([selections[x] == 1 for x in c.unmalted]):
                    return 'IMPOSSIBLE'
                if len(c.malted) == 1:
                    for i in c.malted:
                        selections[i] = 1
                    break
    
    return ' '.join([str(x) for x in selections])
    
if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        N = int(fIn.readline().strip())
        M = int(fIn.readline().strip())
        customers = []
        for i in range(M):
            customers.append(Customer([int(x) for x in \
                            fIn.readline().strip().split()][1:]))
        result = solve(N, M, customers)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
