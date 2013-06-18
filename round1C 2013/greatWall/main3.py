'''
Created on May 27, 2013

@author: Yubin Bai
'''

import time
from bintrees import FastRBTree
import heapq

MAX_DAY = 676061
infinity = (1 << 43)

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
    
    success = False
    attackCounter = 0    

    greatWall = initTree()
    toBeRepaired = initTree()
     
    day = 0
    while len(tribes) > 0 and day < MAX_DAY:
        success = False
        currTribe = heapq.heappop(tribes)
        day = currTribe.d        
        attack = w, e, s = currTribe.w, currTribe.e, currTribe.s

        # test if attack is successful            
        curr, currValue = greatWall.floor_item(w)
        while curr < e:
            if currValue < s:
                success = True
                break
            curr, currValue = greatWall.succ_item(curr)
            
        if success:
            attackCounter += 1
            success = False
            insertToTree(toBeRepaired, attack)
            
        if currTribe.hasNextAttack():
            currTribe.nextAttack()
            heapq.heappush(tribes, currTribe)            
                
        # fix wall at day's end
        if len(tribes) > 0 and day != tribes[0].d:
            iterTree = toBeRepaired.items()
            prev, prevValue = next(iterTree)
            for key, value in iterTree:
                insertToTree(greatWall, (prev, key, prevValue))
                prev, prevValue = key, value
            toBeRepaired = initTree()              
                    
    return attackCounter

def initTree():
    tree = FastRBTree()
    tree[infinity] = 0
    tree[-1 * infinity] = 0
    return tree

def insertToTree(tree, attack):
    west, east, strength = attack
    # keep last segment untouched
    if east not in tree:
        prev, prevValue = tree.floor_item(east)
        if prevValue < strength:
            tree[east] = prevValue
    
    # middle of tree, process max
    curr, currValue = tree.floor_item(west)
    if currValue < strength:
        tree[west] = strength
    
    curr, currValue = tree.floor_item(west)
    while curr < east:
        if currValue < strength:
            tree[curr] = strength
        curr, currValue = tree.succ_item(curr)


if __name__ == '__main__':
    # fInput = open('input.txt')
    fInput = open('C-small-practice.in')
    outFile = open('output.txt', 'w')
    numOfTests = int(fInput.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for test in range(numOfTests):
        nTribes = int(fInput.readline())
        tribes = []
        for x in range(nTribes):
            # d, n, w, e, s, delta_d, delta_p, delta_s  
            tribes.append(Tribe([int(a) for a in fInput.readline().rstrip().split()]))
        
        success = attacks(tribes)
        outFile.write("Case #%d: %d\n" % (test + 1, success))

   
    millis2 = int(round(time.time() * 1000))
    
    print(millis2 - millis1)
