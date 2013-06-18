'''
Created on 2013-6-1

@author: Yubin Bai
'''
import time
infinity = 1 << 32

wallType = {
        (1, 0, 1, 1):'1', \
        (1, 1, 1, 0):'2', \
        (1, 0, 1, 0):'3', \
        (1, 1, 0, 1):'4', \
        (1, 0, 0, 1):'5', \
        (1, 1, 0, 0):'6', \
        (1, 0, 0, 0):'7', \
        (0, 1, 1, 1):'8', \
        (0, 0, 1, 1):'9', \
        (0, 1, 1, 0):'a', \
        (0, 0, 1, 0):'b', \
        (0, 1, 0, 1):'c', \
        (0, 0, 0, 1):'d', \
        (0, 1, 0, 0):'e', \
        (0, 0, 0, 0):'f', \
}

def solve(route1, route2):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    currX = currY = 0
    currD = 3
    rooms = {}
    rooms[(0,0)] = [0] * 4
    
    def walkRoute(currX, currY, currD, route):
        for i, v in enumerate(route):
            if v == 'L':
                currD = (currD + 1) % 4
            elif v == 'W':
                if i > 0 and route1[i - 1] == 'W':
                    leftWall = (currD + 1) % 4  # block left
                    rooms[(currX, currY)][leftWall] = 1
                currX += directions[currD][0]
                currY += directions[currD][1]
                if (currX, currY) not in rooms:
                    rooms[(currX, currY)] = [0] * 4
            else:  # v == 'R'
                if i > 0 and route1[i - 1] == 'W':  # block left
                    leftWall = (currD + 1) % 4
                    rooms[(currX, currY)][leftWall] = 1           
                rooms[(currX, currY)][currD] = 1  # block front
                currD = (currD + 3) % 4
        return currX, currY, currD 
                
    endX, endY, endD = walkRoute(currX, currY, currD, route1)                
    currD = (endD + 2) % 4
    walkRoute(endX, endY, currD, route2)
    del rooms[(0, 0)]
    if (endX, endY) in rooms:
        del rooms[(endX, endY)]

    minX = minY = infinity
    maxX = maxY = -1 * infinity
    for t in rooms:
        minX = min(minX, t[0])
        maxX = max(maxX, t[0])
        minY = min(minY, t[1])
        maxY = max(maxY, t[1])

    result = []
    for y in range(maxY, minY - 1, -1):
        row = []
        for x in range(minX, maxX + 1):
            row.append(wallType[tuple(rooms[(x, y)])])
        result.append(row)
    resultStr = ''
    for row in result:
        resultStr += '\n'
        resultStr += ''.join(row)
    return resultStr

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        route1, route2 = fIn.readline().strip().split()

        result = solve(route1, route2)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
