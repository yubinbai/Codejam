'''
Created on May 30, 2013

@author: Yubin Bai
'''
import time
infinity = (1 << 13)
maxN = 4200
maxL = 5
# wrong solution, can't work with this type
def solve(S):
    size = len(S)
    memo = []
    for i in range(maxN):
        memo.append(list([infinity] * maxL))
    memo[0][4] = 0
    for consumed in range(size):
        for unchanged in range(maxL):
            if memo[consumed][unchanged] == infinity:
                continue
            for w in wordDict:
                nextIndexAllowedToChange = 4 - unchanged
                newUnchanged = unchanged
                countChanges = 0
                good = (len(w) + consumed) <= size
                i = 0
                while (i < len(w)) and good: 
                    newUnchanged += 1
                    if w[i] != S[consumed + i]:
                        newUnchanged = 0
                        if i < nextIndexAllowedToChange:
                            good = False
                            break
                        nextIndexAllowedToChange = i + 5 
                        countChanges += 1
                    i += 1
                if good:
                    newUnchanged = min(newUnchanged, 4)
                    v1 = memo[consumed + len(w)][newUnchanged]
                    v2 = memo[consumed][unchanged] + countChanges
                    memo[consumed + len(w)][newUnchanged] = min(v1, v2)
    return min(memo[size])

wordDict = []

if __name__ == '__main__':
    fDict = open('garbled_email_dictionary.txt')
    wordDict = fDict.read().split()

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
