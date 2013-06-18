'''
Solving the third code jam problem

'''
import math
def nextPalindrome(n):  # find the next palindrome bigger than n, n > 11
    s = str(int(n))
    length = len(s)
    construct = []

    if (length % 2 == 1):  # length is odd
        for i in range(length // 2 + 1):  # save front half to middle
            construct.append(s[i])
        i = length // 2 - 1
        j = length // 2 + 1
        while j < length: 
            if (s[i] != s[j]):
                break;
            i -= 1
            j += 1
        if j == length or s[i] < s[j]:  # n is palindrome, or the front is smaller
            num = int(''.join(construct))  # use the front part, increase one, construct
            num += 1
            numStrList = list(str(num))
            for i in range(length // 2 - 1, -1, -1):
                numStrList.append(numStrList[i])
            return int(''.join(numStrList))
        else:  # not a palindrome, but front is larger, use front to construct
            for i in range(length // 2 - 1, -1, -1):      
                construct.append(construct[i])
            return int(''.join(construct))
        
    else:  # length is even
        for i in range(length // 2):  # save front half to middle
            construct.append(s[i])
        if (s[length // 2 - 1] == s[length // 2]):  # possibly a palindrome itself
            i = length // 2 - 1
            j = length // 2
            while j < length: 
                if (s[i] != s[j]):
                    break;
                i -= 1
                j += 1
                
            if j == length or s[i] < s[j]:  # n is palindrom, or the front is smaller
                num = int(''.join(construct))  # use the front part, increast one, construct
                num += 1
                numStrList = list(str(num))
                
                for i in range(length // 2 - 1, -1, -1):
                    numStrList.append(numStrList[i])
                return int(''.join(numStrList))
            else:  # not a palindrome, but front is larger, use front to construct
                for i in range(length // 2 - 1, -1, -1):
                    construct.append(construct[i])
                return int(''.join(construct))
        elif s[length // 2 - 1] < s[length // 2]:  # front is smaller
            num = int(''.join(construct))  # use the front part, increast one, construct
            num += 1
            numStrList = list(str(num))
            for i in range(length // 2 - 1, -1, -1):
                numStrList.append(numStrList[i])
            return int(''.join(numStrList))
        else:  # back is larger
            for i in range(length // 2 - 1, -1, -1):
                construct.append(construct[i])
            return int(''.join(construct))    
                
def isSquareFair(number):
    root = math.floor(math.sqrt(number))
    return root ** 2 == number and root == nextPalindrome(root - 1)

def fairAndSquareBetween(start, end):
    results = []
    palin = nextPalindrome(start - 1)
    while palin <= end:
        if isSquareFair(palin):
            results.append(palin)
        palin = nextPalindrome(palin)
    return list(results)

if __name__ == "__main__":        
    # main program
    memo = fairAndSquareBetween(1, 10 ** 14)    
    print(memo)
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
