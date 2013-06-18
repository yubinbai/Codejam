'''
Created on 2013-5-12

@author: Administrator
'''
MAX_DAY = 676061
import heapq

class Tribe:
    def __init__(self, data):
        self.d, self.n, self.w, self.e, self.s, self.delta_d, self.delta_p, self.delta_s = data
        self.n -= 1
    def hasNextAttack(self):
        return self.n > 0
    def nextAttack(self):
        self.d += self.delta_d
        self.w += self.delta_p
        self.e += self.delta_p
        self.s += self.delta_s
        self.n -= 1
    def __lt__(self, other):
        return self.d < other.d
        

def attacks(tribes):
    heapq.heapify(tribes)
    counter = 0
    greatWall = {}
    toBeRepaired = {}
    
    day = 0
    while len(tribes) > 0 and day < MAX_DAY:
        success = False
        currTribe = heapq.heappop(tribes)
        day = currTribe.d
        
        for pos in range(currTribe.w, currTribe.e):
            if pos not in greatWall or greatWall[pos] < currTribe.s:
                success = True
                if pos in toBeRepaired:
                    toBeRepaired[pos] = max(currTribe.s, toBeRepaired[pos]) 
                else:
                    toBeRepaired[pos] = currTribe.s
        if success:
            counter += 1
            success = False
        if currTribe.hasNextAttack():
            currTribe.nextAttack()
            heapq.heappush(tribes, currTribe)
        if len(tribes) > 0 and day != tribes[0].d:
            for i in toBeRepaired:
                greatWall[i] = toBeRepaired[i]
            toBeRepaired = {}
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
            tribes.append(Tribe([int(a) for a in fInput.readline().rstrip().split()]))
        
        success = attacks(tribes)
        outFile.write("Case #%d: %d\n" % (test + 1, success))
