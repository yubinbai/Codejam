import time
def getGain(E, R, N, value):

    memo = [-1] * (E + 1)
    prevMemo = [-1] * (E + 1)

    # last activity
    for i in range(E + 1):
        memo[i] = value[-1] * i
    
    for step in range(N - 2, -1, -1):
        for e in range(E + 1):
            currMax = 0
            for consume in range(e, -1, -1):
                next = e - consume + R
                if next > E:
                    next = E
                thisGain = consume * value[step] + memo[next]
                if thisGain > currMax:
                    currMax = thisGain
            prevMemo[e] = currMax
        temp = prevMemo
        prevMemo = memo
        memo = temp
    return memo[E]

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
