'''
Created on 2013-6-2

@author: Yubin Bai
based on permutation and count solution by brute force
'''
import time
infinity = 1 << 25


def solve(N, names, prices):
    result = []
    while True:
        invertedCount = [0] * N
        for i in range(N):
            for j in range(i):
                if prices[i] < prices[j]:
                    invertedCount[i] += 1
            for j in range(i + 1, N):
                if prices[j] < prices[i]:
                    invertedCount[i] += 1
        maxInverted, maxCount = [], 0
        for i, v in enumerate(invertedCount):
            if v == maxCount:
                maxInverted.append(i)
            elif v > maxCount:
                maxInverted = [i]
                maxCount = v
        if maxCount == 0:
            break
        changeI, changeName = -1, '~'
        for i in maxInverted:
            if names[i] < changeName:
                changeI, changeName = i, names[i]
        prices[changeI] = (max(prices[:changeI] + [0]) + min(
            prices[changeI + 1:] + [infinity])) / 2.0
        result.append(changeName)

    result.sort()
    return ' '.join(result)

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())

    millis1 = int(round(time.time() * 1000))

    for t in range(numOfTests):
        names = fIn.readline().strip().split()
        prices = [int(x) for x in fIn.readline().strip().split()]
        result = solve(len(prices), names, prices)
        fOut.write("Case #%d: %s \n" % (t + 1, result))

    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
