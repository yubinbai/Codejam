'''
Created on May 30, 2013

@author: Yubin Bai
'''
import time
infinity = (1 << 13)
maxL = 5


def solve(S):
    size = len(S)
    memo = {}
    memo[(0, 4)] = 0
    for consumed in range(size):
        for unchanged in range(maxL):
            if (consumed, unchanged) not in memo:
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
                    v1 = infinity
                    if (consumed + len(w), newUnchanged) in memo:
                        v1 = memo[(consumed + len(w), newUnchanged)]
                    v2 = memo[(consumed, unchanged)] + countChanges
                    memo[(consumed + len(w), newUnchanged)] = min(v1, v2)
    currMin = infinity
    for x in range(maxL):
        if (size, x) in memo:
            currMin = min(currMin, memo[(size, x)])
    return currMin

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
