'''
Created on 2013-5-29

@author: Yubin Bai
'''
def getInput(message):
    keyMap = {'a':'2', 'b':'22', 'c':'222', 'd':'3', 'e':'33', \
              'f':'333', 'g':'4', 'h':'44', 'i':'444', 'j':'5', \
              'k':'55', 'l':'555', 'm':'6', 'n':'66', 'o':'666', \
              'p':'7', 'q':'77', 'r':'777', 's':'7777', 't':'8', \
              'u':'8', 'v':'88', 'w':'9', 'x':'99', 'y':'999', \
              'z':'9999', ' ':'0'}
    result = ''
    for i in range(len(message)):
        if len(result) > 0 and result[-1] == keyMap[message[i]][0]:
            result += ' '
        result += keyMap[message[i]]
    return result

if __name__ == "__main__":        
    f = open('input.txt')
    outFile = open('output.txt', 'w')
    numOfTests = int(f.readline())
    results = []
    for test in range(numOfTests):
        result = getInput(f.readline().rstrip('\n'))
        outFile.write("Case #%d: %s\n" % (test + 1, result))
