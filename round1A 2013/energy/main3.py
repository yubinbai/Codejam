import time
def getGain(E, R, N, value):
    if R > E:
        R = E
    use = [E]
    for i in range(1, len(value)):
        use.append(R)
        for j in range(i - 1, -1, -1):
            if value[j] >= value[i]:
                break
            if use[j] + use[i] < E:
                use[i] += use[j]
                use[j] = 0
            else:
                use[j] -= E - use[i]
                use[i] = E
                break
    currGain = sum([value[i] * use[i] for i in range(len(value))])    
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
