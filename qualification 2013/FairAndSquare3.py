'''
Solving the third code jam problem

'''
def nextPalindrome(n): # find the next palindrome bigger than n, n > 11
	s = ''
	s = str(n)
	length = len(s)
	construct = []

	if (length % 2 == 1): # length is odd
		for i in range(length/2 + 1): # save front half to middle
			construct.append(s[i])
			
		i = length/2 -1
		j = length/2 + 1
		while j < length: 
			if (s[i] != s[j]):
				break;
			i -= 1
			j += 1
		
		if j == length or s[i] < s[j]:     # n is palindrom, or the front is smaller
			num = int(''.join(construct)) # use the front part, increast one, construct
			num += 1
			numStrList = list(str(num))
			
			for i in range(length/2-1, -1, -1):
				numStrList.append(numStrList[i])
			return int(''.join(numStrList))
		else: #not a palindrome, but front is larger, use front to construct
			for i in range(length/2 -1, -1, -1):      
				construct.append(construct[i])
			return int(''.join(construct))
	else: # length is even
		for i in range(length/2): # save front half to middle
			construct.append(s[i])
		if (s[length/2 - 1] == s[length/2]): # possibly a palindrom itself
			i = length/2 -1
			j = length/2
			while j < length: 
				if (s[i] != s[j]):
					break;
				i -= 1
				j += 1
				
			if j == length or s[i] < s[j]:     # n is palindrom, or the front is smaller
				num = int(''.join(construct)) # use the front part, increast one, construct
				num += 1
				numStrList = list(str(num))
				
				for i in range(length/2-1, -1, -1):
					numStrList.append(numStrList[i])
				return int(''.join(numStrList))
			else: #not a palindrome, but front is larger, use front to construct
				for i in range(length/2-1, -1, -1):
					construct.append(construct[i])
				return int(''.join(construct))
		elif s[length/2-1] < s[length/2]: # front is smaller
			num = int(''.join(construct)) # use the front part, increast one, construct
			num += 1
			numStrList = list(str(num))
			for i in range(length/2 -1, -1, -1):
				numStrList.append(numStrList[i])
			return int(''.join(numStrList))
		else: # back is larger
			for i in range(length/2-1, -1, -1):
				construct.append(construct[i])
			return int(''.join(construct))	
				
def isSquareFair(number):
	import math
	root = long(math.sqrt(number))
	return root**2 == number and root == nextPalindrome(root-1)

def fairAndSquareBetween((start, end)):
	results = []
	palin = nextPalindrome(start-1)
	while palin <= end:
		if isSquareFair(palin):
			results.append(palin)
		palin = nextPalindrome(palin)
	return list(results)

if __name__ == "__main__":		
	# main program
	import os, math
	
	full_path = os.path.realpath(__file__)
	path, file = os.path.split(full_path)

	f = open(path + '\\' + 'C-large-1.in')
	numOfTests = int(f.readline())
	
	# construct memo
	from multiprocessing import Pool
	pool = Pool(processes=6)
	
	intervals = []
	for i in range(10):
		intervals.append((i*10**99+1, (i+1) * 10**99))
	
	memo = pool.map(fairAndSquareBetween, intervals, 1)	

	
	memo = sum(memo, [])
	#print 'memo', memo

	results = []
	for test in range(numOfTests):
		a, b = [long(x) for x in f.readline().split()] # read a line
		resultCounter = 0
		
		# search for in between
		for i in range(len(memo)):
			if memo[i] > b:
				break
			if memo[i] >= a:
				resultCounter += 1
			
		results.append(resultCounter)
		
	outFile = open(path + '\\' + 'memo.txt', 'w')

	for i in range(len(memo)):
		outFile.write("%d\n" % (memo[i]))
