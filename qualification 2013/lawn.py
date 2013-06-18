'''
Solving the second code jam problem

'''
def isPossible(n, m, matrix):
	#get the largest ones from left, right, top bottom
	#cannot happen with more than two of them not being the origin position
	largestLeftIndex = [[0 for x in range(m)] for y in range(n)]
	for i in range(n):
		for j in range(1, m):
			if matrix[i][j] >= matrix[i][largestLeftIndex[i][j-1]]:
				largestLeftIndex[i][j] = j
			else:
				largestLeftIndex[i][j] = largestLeftIndex[i][j-1]
	
	largestRightIndex = [[m-1 for x in range(m)] for y in range(n)]
	for i in range(n):
		for j in range(m-2,-1,-1):
			if matrix[i][j] >= matrix[i][largestRightIndex[i][j+1]]:
				largestRightIndex[i][j] = j				
			else:
				largestRightIndex[i][j] = largestRightIndex[i][j+1]
	
	largestTopIndex = [[0 for x in range(m)] for y in range(n)]
	for i in range(1,n):
		for j in range(m):
			if matrix[i][j] >= matrix[largestTopIndex[i-1][j]][j]:
				largestTopIndex[i][j] = i			
			else:
				largestTopIndex[i][j] = largestTopIndex[i-1][j]
	
	largestBottomIndex = [[n-1 for x in range(m)] for y in range(n)]
	for i in range(n-2,-1,-1):
		for j in range(m):
			if matrix[i][j] >= matrix[largestBottomIndex[i+1][j]][j]:
				largestBottomIndex[i][j] = i
			else:
				largestBottomIndex[i][j] = largestBottomIndex[i+1][j]
	
	for i in range(n):
		for j in range(m):				
			horizontalDiff = largestLeftIndex[i][j] != j or largestRightIndex[i][j] != j
			verticalDiff = largestTopIndex[i][j] != i or largestBottomIndex[i][j] != i
				
			if horizontalDiff and verticalDiff:
				return False
	return True

				
# main program
import os
full_path = os.path.realpath(__file__)
path, file = os.path.split(full_path)

f = open(path + '\\' + 'B-large.in')
numOfTests = int(f.readline())

results = []
for test in range(numOfTests):
	data = []
	n, m = [int(x) for x in f.readline().split()] # read first line
	
	for i in range(n):
		data.append([int(x) for x in f.readline().split()])

	results.append(isPossible(n, m, data))

outFile = open(path + '\\' + 'output.txt', 'w')

for i in range(0, len(results)):
	caseNumber = i+1
	if results[i]:
		outFile.write("Case #%d: YES\n" % caseNumber )
	else: 
		outFile.write("Case #%d: NO\n" % caseNumber )
