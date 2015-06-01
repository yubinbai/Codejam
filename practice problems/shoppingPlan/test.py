'''
Created on Jun 6, 2013

@author: Yubin Bai
'''
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
    
    print(getSubsets(list('abc')))