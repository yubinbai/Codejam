'''
Created on 2013-5-12

@author: Yubin Bai
'''
MAX_DAY = 676061
from collections import defaultdict

def attacks(nTribes, tribes):
    attacksEachDay = defaultdict(list)
    # d, n, w, e, s, delta_d, delta_p, delta_s
    for tribe in tribes:
        d, n, w, e, s, delta_d, delta_p, delta_s = tribe
        while n > 0:
            attacksEachDay[d].append((w, e, s))
            d += delta_d
            w += delta_p
            e += delta_p
            s += delta_s
            n -= 1
            
    # memory of great wall is too large, need to use interval tree
    success = False
    counter = 0
    greatWall = {}
    for day in range(MAX_DAY):
        if day in attacksEachDay:
            toBeRepaired = {}
            for attack in attacksEachDay[day]:
                w, e, s = attack
                for pos in range(w, e):
                    if pos not in greatWall or greatWall[pos] < s:
                        success = True
                        if pos in toBeRepaired:
                            toBeRepaired[pos] = max(s, toBeRepaired[pos]) 
                        else:
                            toBeRepaired[pos] = s
                if success:
                    counter += 1
                    success = False
            for i in toBeRepaired:
                greatWall[i] = toBeRepaired[i]
    return counter


if __name__ == '__main__':
    fInput = open('C-small-attempt0.in')
    outFile = open('output.txt', 'w')
    numOfTests = int(fInput.readline())
    
    for test in range(numOfTests):
        nTribes = int(fInput.readline())
        tribes = []
        for x in range(nTribes):
            # d, n, w, e, s, delta_d, delta_p, delta_s  
            tribes.append([int(a) for a in fInput.readline().rstrip().split()])
        
        success = attacks(nTribes, tribes)
        outFile.write("Case #%d: %d\n" % (test + 1, success))
