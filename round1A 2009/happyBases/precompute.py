'''
Created on Jun 12, 2013

@author: Administrator
'''
import pickle
import time

maxN = 2000
SQUARE = dict([(c, int(c) ** 2) for c in "0123456789"])
   
def toBase(base, n):
    result = []
    while n != 0:
        result.append(str(n % base))
        n //= base
    result.reverse()
    return int(''.join(result))

if __name__ == '__main__':
    d = []
    for i in range(11):
        d.append(set())
    
    def isHappy(n, base):
        original = n
        s = set()
        while (n > 1) and (n not in s):
            s.add(n)
            n = toBase(base, n)
            n = toBase(10, sum(SQUARE[d] for d in str(n)))
            if n in d[base]:
                return True
            if n < maxN:
                return False
        return n == 1
        
    millis1 = int(round(time.time() * 1000))
        
    for i in range(maxN):
        for b in range(2, 11):
            if isHappy(i, b):
                d[b].add(i)
                
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))
    
    pickle.dump(d, open("memo.dat", 'w'))
