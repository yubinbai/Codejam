'''
Created on May 27, 2013

@author: Yubin Bai
'''

import time
from bintrees import FastRBTree
from collections import defaultdict

MAX_DAY = 676061
infinity = (1 << 43)

def attacks(tribes):
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
                
    success = False
    attackCounter = 0    

    greatWall = initTree()
    toBeRepaired = initTree()
     
    day = 0
    for day in range(MAX_DAY):
        if day in attacksEachDay:
            for attack in attacksEachDay[day]:
                success = False     
                w, e, s = attack
        
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

            # fix wall at day's end
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
    visitedKeys = []
    while curr < east:
        visitedKeys.append(curr)
        if currValue < strength:
            tree[curr] = strength
        curr, currValue = tree.succ_item(curr)
    
    if len(visitedKeys) > 0:
        prev = visitedKeys[0]
        for i in range(1, len(visitedKeys)):
            if tree[prev] == tree[visitedKeys[i]]:
                del tree[visitedKeys[i]]
            else:
                prev = visitedKeys[i]

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
            tribes.append([int(a) for a in fInput.readline().rstrip().split()])
        
        success = attacks(tribes)
        outFile.write("Case #%d: %d\n" % (test + 1, success))

    millis2 = int(round(time.time() * 1000))
    
    print(millis2 - millis1)
