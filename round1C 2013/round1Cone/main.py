'''
Created on 2013-5-12

@author: Administrator
'''
def nValue(str, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    size = len(str)
    
    # find the regions by scanning
    regions = []
    left = 0
    right = 0
    while right < size:
        while str[right] not in vowels:
            if right - left == n - 1:
                regions.append((left, right))
                left += 1
            right += 1
            if right > size - 1:
                break
        left = right + 1
        right = left        
    
    # construct the intervals
    left = 0
    right = size - 1
    counter = 0
    for t in regions:
        left1, right1 = t
        counter += (left1 - left + 1) * (right - right1 + 1)  # start in left1, one over count
        left = left1 + 1
    return counter
    
if __name__ == '__main__':
    fInput = open('A-large.in')
    outFile = open('output.txt', 'w')
    numOfTests = int(fInput.readline())
    
    for test in range(numOfTests):
        str, n = fInput.readline().rstrip().split()  # read a line
        outFile.write("Case #%d: %d\n" % (test + 1, nValue(str, int(n))))
    
    
    
    
    
