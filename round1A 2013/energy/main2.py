import time
def getGain(E, R, N, value):
    if R > E:
        R = E
    size = len(value)
    upper = [E] * size
    lower = [0] * size
    currGain = 0
    while True:
        currMaxI, currMax = -1, -1
        for i, v in enumerate(value):
            if currMax < v and upper[i] > lower[i]:
                currMaxI, currMax = i, v
        if currMax == -1:
            break
        currGain += (upper[currMaxI] - lower[currMaxI]) * currMax
        upper[currMaxI] = -1
        for i in range(currMaxI + 1, size):
            if upper[i] > (i - currMaxI) * R:
                upper[i] = (i - currMaxI) * R
        for i in range(currMaxI):
            reserve = max(0, E - (currMaxI - i) * R)
            if lower[i] < reserve:
                lower[i] = reserve
    return currGain

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        E, R, N = [int(x) for x in fIn.readline().split()]
        value = [int(x) for x in fIn.readline().split()]
        result = getGain(E, R, N, value)
        fOut.write("Case #%d: %d \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print(millis2 - millis1)

    fIn.close()
    fOut.close()
