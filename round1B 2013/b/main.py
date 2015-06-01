'''
Created on May 30, 2013

@author: Yubin Bai
'''
import time


def solve(N, x, y):
    currSum = size = 1
    while currSum + 2 * (size + 2) - 1 <= N:
        currSum += 2 * (size + 2) - 1
        size += 2
    if abs(x - y) in range(0, size, 2) and abs(x + y) in range(0, size, 2):
        return 1.0
    if abs(x - y) > (size + 1) or abs(x - y) % 2 != 0:
        return 0.0
    # on the edge
    outerLayer = N - currSum
    # distanceToBottom = y, need P(i > y)
    if outerLayer < y:
        return 0.0
    if outerLayer < size + 2:
        pass
    else:
        overflow = outerLayer - (size + 1)
        outerLayer -= 2 * overflow
        y -= overflow
    combSum = 0
    for i in range(y + 1):
        combSum += comb(outerLayer, i)
    return 1 - combSum * 1.0 / (2 ** outerLayer)


def comb(n, k):
    return fact(n) / (fact(k) * fact(n - k))

factMemo = {0: 1, 1: 1}


def fact(n):
    if n in factMemo:
        return factMemo[n]
    factMemo[n] = n * fact(n - 1)
    return factMemo[n]

if __name__ == '__main__':
    # fIn = open('input.txt')
    # fIn = open('B-small-practice.in')
    fIn = open('B-large-practice.in')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())

    millis1 = int(round(time.time() * 1000))

    for t in range(numOfTests):
        N, x, y = [int(x) for x in fIn.readline().split()]

        result = solve(N, x, y)

        fOut.write("Case #%d: %f \n" % (t + 1, result))

    millis2 = int(round(time.time() * 1000))
    print(millis2 - millis1)

    fIn.close()
    fOut.close()
