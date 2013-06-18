'''
Created on May 30, 2013

@author: Yubin Bai
'''
import time
def solve(currSum, array):
    i = 0 
    while i < len(array) and array[i] < currSum:
        currSum += array[i]
        i += 1
    if i == len(array) or len(array) == 0:
        return 0
    addCounter = 0
    if currSum == 1:
        return len(array) - i
    while currSum <= array[i]:
        currSum = 2 * currSum - 1
        addCounter += 1
    # by adding 
    result1 = addCounter + solve(currSum + array[i], array[i + 1:])
    result2 = len(array) - i
    return min(result1, result2)

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        A, N = [int(x) for x in fIn.readline().split()]
        array = [int(x) for x in fIn.readline().split()]
        array.sort()
        result = solve(A, array)

        fOut.write("Case #%d: %d \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print(millis2 - millis1)

    fIn.close()
    fOut.close()
