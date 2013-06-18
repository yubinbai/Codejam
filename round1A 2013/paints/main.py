def paintUsed(r, k):
    return (2 * r - 1 + 2 * k) * k

def getRings(par):
    r, t = par
    result, low, high = 0, 1, t
    while low <= high:
        mid = (low + high) // 2
        if paintUsed(r, mid) > t:
            high = mid - 1
        else:
            low, result = mid + 1, mid 
    return result

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())

    for t in range(numOfTests):
        r, paint = [long(x) for x in fIn.readline().split()]
        result = getRings((r, paint))

        fOut.write("Case #%d: %d \n" % (t + 1, result))

