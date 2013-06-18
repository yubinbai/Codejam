'''
Created on 2013-5-29

@author: Administrator
'''
def getSum(currSum, values):
    size = len(values)
    for i in range(size):
        for j in range(i + 1, size):
            if values[i] + values[j] == currSum:
                return i + 1, j + 1
    
if __name__ == "__main__":        
    f = open('input.txt')
    outFile = open('output.txt', 'w')
    numOfTests = int(f.readline())
    results = []
    for test in range(numOfTests):
        C = int(f.readline())  # read a line
        f.readline()
        values = [int(x) for x in f.readline().split()]  # read a line
        a, b = getSum(C, values)
        outFile.write("Case #%d: %d %d\n" % (test + 1, a, b))
