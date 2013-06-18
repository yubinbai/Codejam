'''
Created on 2013-6-6

@author: Yubin Bai
'''
import time
import math
from memoized import memoized

infinity = 1 << 62

class Store:
    def __init__(self, data):
        self.x = int(data[0])
        self.y = int(data[1])
        self.items = {}
        for line in data[2:]:
            item, price = line.split(':')
            self.items[item] = int(price)
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    def hasItems(self, items):
        for i in items:
            if i not in self.items:
                return False
        return True
    
def solve(gasP, items, stores):
    home = Store([0, 0])
    @memoized
    def cost(itemsHad, currStore):
        itemsToGet = set(items) - itemsHad
        
        if len(itemsToGet) == 0:
            return currStore.distance(home) * gasP
        subSets = getSubsets(itemsToGet)
        currMin = infinity
        for s in subSets:
            for store in stores:
                if store.hasItems(s):
                    cost1 = currStore.distance(store) * gasP
                    for i in s:
                        cost1 += store.items[i]
                    cost1 += cost(frozenset(itemsHad | s), store)
                    currMin = min(currMin, cost1)
        return currMin
    return '%.7F' % cost(frozenset(), home)

def getSubsets(items):
    it = list(items)
    subsets = []
    path = []
    def subset(step):
        if step == len(items):
            subsets.append(frozenset(path))
            return
        subset(step + 1)
        path.append(it[step])
        subset(step + 1)
        path.pop()
    subset(0)
    del subsets[0]
    return subsets      

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        nItem, nStore, gasP = map(int, fIn.readline().strip().split())
        items = fIn.readline().strip().split()
        stores = []
        for i in range(nStore):
            stores.append(Store(fIn.readline().strip().split()))
        result = solve(gasP, items, stores)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
