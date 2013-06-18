'''
Created on May 28, 2013

@author: Yubin Bai

First, if we want to reach the target in N moves, we have to have 1 + 2 + ... +
N >= |X| + |Y|. Moreover, if we want to reach the target in N moves, the parity
of the numbers 1 + 2 + ... + N and |X| + |Y| has to be the same. This is because
the parity of the sum of the lengths of jumps we make in the North-South
direction has to match the parity of |Y|, and the sum of lengths of West-East
jumps has to match the parity of |X|. It turns out that if N satisfies these two
conditions, it is possible to reach (X, Y) with N jumps.

'''
def solve(x, y):
    N = 0
    currSum = 0
    while currSum < abs(x) + abs(y) or (currSum + x + y) % 2 == 1:
        N += 1
        currSum += N
    result = ""
    while N > 0:
        if abs(x) > abs(y):
            if x > 0: 
                result += 'E'
                x -= N
            else:
                result += 'W'
                x += N
        else:
            if y > 0:
                result += 'N'
                y -= N
            else:
                result += 'S'
                y += N
        N -= 1
    return result[::-1]

if __name__ == '__main__':
    # fInput = open('input.txt')
    fInput = open('input.txt')
    outFile = open('output.txt', 'w')
    numOfTests = int(fInput.readline())
    
    for test in range(numOfTests):
        x, y = [int(x) for x in fInput.readline().strip().split()]
        result = solve(x, y)
        
        outFile.write("Case #%d: %s\n" % (test + 1, result))

    fInput.close()
    outFile.close()
