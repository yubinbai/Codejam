'''
Created on 2013-5-12

@author: Administrator
'''
def recur(currX, currY, targetX, targetY, step, result):
    if step > 500:
        return False
    if currX == targetX and currY == targetY:
        return True
    
    # E
    result.append('E')
    if recur(currX+step, currY, targetX, targetY, step+1, result):
        return True
    result.pop()
    
    # W
    result.append('W')
    if recur(currX-step, currY, targetX, targetY, step+1, result):
        return True
    result.pop()
    
    # N
    result.append('N')
    if recur(currX, currY+step, targetX, targetY, step+1, result):
        return True
    result.pop()
    
    # S
    result.append('S')
    if recur(currX, currY-step, targetX, targetY, step+1, result):
        return True
    result.pop()

if __name__ == '__main__':
    fInput = open('input.txt')
    outFile = open('output.txt', 'w')
    numOfTests = int(fInput.readline())
    
    for test in range(numOfTests):
        x, y = fInput.readline().rstrip().split()  # read a line
        result = []
        recur(0, 0, x, y, 1, result)
        outFile.write("Case #%d: %s\n" % (test + 1, ''.join(result)))