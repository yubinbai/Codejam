'''
Created on May 28, 2013

@author: Yubin Bai
'''

import time
from bisect import bisect

infinity = (1 << 30)

def attacks(tribes):
    class attack:
        def __init__(self, w, e, s, d):
            self.w, self.e, self.s, self.d = w, e, s, d
        def __lt__(self, other):
            return self.d < other.d
    
    attacksEachDay = []
    points = set()
    # d, n, w, e, s, delta_d, delta_p, delta_s
    for tribe in tribes:
        d, n, w, e, s, delta_d, delta_p, delta_s = tribe
        while n > 0:
            points.add(w)
            points.add(e)
            attacksEachDay.append(attack(w, e, s, d))
            d += delta_d
            w += delta_p
            e += delta_p
            s += delta_s
            n -= 1

    attacksEachDay.sort()
    points = list(points)
    points.sort()
    numOfPoints = len(points)
            
    for attack in attacksEachDay:
        attack.w = bisect(points, attack.w, 0, numOfPoints) - 1
        attack.e = bisect(points, attack.e, 0, numOfPoints) - 1
                
    treeSize = 1
    while treeSize < numOfPoints - 1 :
        treeSize *= 2
    treeMin = [0] * (treeSize * 2)
    
    # test the attacks 
    answer = 0
    today = 0
    toBeRepaired = []
    for attack in attacksEachDay:
        if attack.d != today:         
            for pastAttack in toBeRepaired:
                treeUpdate(treeMin, treeSize, pastAttack)
            toBeRepaired = []
            today = attack.d
        if getTreeMin(treeMin, treeSize, attack.w, attack.e) < attack.s:
            answer += 1
            toBeRepaired.append(attack)    
    return answer

def getTreeMin(treeMin, treeSize, west, east):
    return _treeMin(treeMin, treeSize, 1, 0, treeSize, west, east)

def _treeMin(treeMin, treeSize, curr, left, right, west, east):
    if west >= right or east <= left:
        return infinity
    answer = treeMin[curr]
    if west > left or east < right:
        mid = (left + right) // 2
        answer = max(answer, min(_treeMin(treeMin, treeSize, curr * 2, left, mid, west, east), \
                            _treeMin(treeMin, treeSize, curr * 2 + 1, mid, right, west, east)))
    return answer

def treeUpdate(treeMin, treeSize, attack):
    west, east, strength = attack.w, attack.e, attack.s
    _treeUpdate(treeMin, treeSize, 1, 0, treeSize, west, east, strength)
    
def _treeUpdate(treeMin, treeSize, curr, left, right, west, east, value):
    if west >= right or east <= left:
        return
    if west <= left and right <= east:
        treeMin[curr] = max(treeMin[curr], value)
    else:
        mid = (left + right) // 2
        _treeUpdate(treeMin, treeSize, curr * 2, left, mid, west, east, value)
        _treeUpdate(treeMin, treeSize, curr * 2 + 1, mid, right, west, east, value)
        treeMin[curr] = max(treeMin[curr], min(treeMin[curr * 2], treeMin[curr * 2 + 1]))
        
if __name__ == '__main__':
    #fInput = open('input.txt')
    fInput = open('C-small-practice.in')
    outFile = open('output.txt', 'w')
    numOfTests = int(fInput.readline())

    millis1 = int(round(time.time() * 1000))
    
    for test in range(numOfTests):
        nTribes = int(fInput.readline())
        tribes = []
        for x in range(nTribes):
            # d, n, w, e, s, delta_d, delta_p, delta_s  
            tribes.append([int(a) for a in fInput.readline().strip().split()])
        
        success = attacks(tribes)
        outFile.write("Case #%d: %d\n" % (test + 1, success))

    millis2 = int(round(time.time() * 1000))
    
    print(millis2 - millis1)
