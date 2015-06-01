'''
Created on May 30, 2013

@author: Yubin Bai
'''
# wrong solution
import time
infinity = (1 << 13)

def solve(S):
    memo = {}
    return min([_solve(S, len(S), x , memo) for x in range(5)]) 

def _solve(S, i, k, memo):
    if i <= 0:
        return 0
    if (i, k) in memo:
        return memo[(i, k)]
    currMin = infinity
    for w in wordDict:
        if len(w) > len(S):
            continue
        changed, firstPos, lastPos = sub(S[len(S) - len(w):], w)
        if changed == -1:
            continue
        for k2 in range(len(S) - len(w)):
            prefixResult = _solve(S, i - len(w), k2, memo)
            if prefixResult != infinity and k2 + firstPos >= 5:
                result = prefixResult + changed
                if lastPos == k:
                    currMin = min(result, currMin)
                elif (i, lastPos) in memo:
                    memo[(i, lastPos)] = min(result, memo[(i, lastPos)])
                else:
                    memo[(i, lastPos)] = result
                              

    memo[(i, k)] = currMin
    return currMin

def sub(s, w):
    # firstPos and lastPos cannot be bigger than five
    firstPos = lastPos = -1
    changes = 0
    size = len(s)
    for i in range(size):
        if s[i] != w[i]:
            changes += 1
            if firstPos == -1:
                firstPos = lastPos = i
            if i != lastPos and i - lastPos <= 5:
                return -1, -1, -1
            else:
                lastPos = i
    if changes == 0:
        firstPos = lastPos = 0
    else:
        firstPos += 1
        lastPos = len(s) - lastPos + 1
    return changes, firstPos, lastPos

wordDict = set()

if __name__ == '__main__':
    fDict = open('garbled_email_dictionary.txt')
    wordDict = set(fDict.read().split())

    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        line = fIn.readline().strip()
        
        result = solve(line)

        fOut.write("Case #%d: %d \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
