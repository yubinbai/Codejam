'''
Created on 2013-5-29

@author: Yubin Bai
'''
def generateRoots():
    path = []
    results = []
    for i in range(3):
        path = [str(i + 1)]
        _generateRoot(1, 26, (i + 1) ** 2, path, results)
    return results

def _generateRoot(step, size, sumSquare, path, results):
    if sumSquare > 9:
        return 
    if step == size:
        return
    oddPalin = oddMirror(path)
    evenPalin = evenMirror(path)
    oddFair = oddPalin ** 2
    if isPalindrome(oddFair):
        results.append(oddFair)
    evenFair = evenPalin ** 2
    if isPalindrome(evenFair):
        results.append(evenFair)
    for i in range(4):
        path.append(str(i))
        _generateRoot(step + 1, size, sumSquare + i * i, path, results)
        path.pop()

def oddMirror(path):
    revPath = path[::-1]
    newPath = path + revPath[1:]
    return int(''.join(newPath))
def evenMirror(path):
    newPath = path + path[::-1]
    return int(''.join(newPath))
def isPalindrome(number):
    numStr = str(number)
    return numStr == numStr[::-1]

if __name__ == '__main__':
    memo = generateRoots()
    memo.sort()
    
    f = open('C-large-1.in')
    outFile = open('output.txt', 'w')
    numOfTests = int(f.readline())
    results = []
    for test in range(numOfTests):
        a, b = [int(x) for x in f.readline().split()]  # read a line
        resultCounter = 0
        # search for in between
        for i in range(len(memo)):
            if memo[i] > b:
                break
            if memo[i] >= a:
                resultCounter += 1
        outFile.write("Case #%d: %d\n" % (test + 1, resultCounter))
