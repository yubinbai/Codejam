'''
Solving the third code jam problem

'''
def isPalindrome(number):
	original = number
	reverse = 0
	while number != 0:
		reverse = reverse * 10 + number % 10
		number /= 10
	return reverse == original

				
# main program
import os, math
full_path = os.path.realpath(__file__)
path, file = os.path.split(full_path)

f = open(path + '\\' + 'C-small-attempt0.in')
numOfTests = int(f.readline())

results = []
for test in range(numOfTests):
	a, b = [int(x) for x in f.readline().split()] # read a line
	counter = 0
	root = int(math.sqrt(a))
	square = int(root**2)
	#in case it's truncated
	if square < a:
		root += 1
		square = root**2
	
	while square <= b:
		if isPalindrome(root) and isPalindrome(square):
			counter += 1 
		square += root * 2 + 1 # (x+1)^2 = x^2 + 2x + 1
		root += 1

	results.append(counter)

outFile = open(path + '\\' + 'output.txt', 'w')

for i in range(0, len(results)):
	caseNumber = i+1
	outFile.write("Case #%d: %d\n" % (caseNumber, results[i] ))
