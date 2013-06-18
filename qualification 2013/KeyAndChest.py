'''
Solving the fourth code jam problem

'''
import os, copy
from collections import Counter
def keySequence((K, N, startKeys, chestKeyType, chestContents)):
	currentKeys = [0 for x in range(201)]
	keySet = set()
	for i in range(len(chestKeyType)):
		keySet.add(chestKeyType[i])
	
	for i in startKeys:
		currentKeys[i] += 1
	
	chestIsClosed = [True for x in range(N)]
	stack = []
	if keySequenceHelper(N, currentKeys, keySet, chestKeyType, chestContents, 0, chestIsClosed, stack):
		return list(stack)
	else:
		return None
	

def keySequenceHelper(N, currentKeys, keySet, chestKeyType, chestContents, step, chestIsClosed, stack):
	if step >= N:
		for i in range(N):
			if chestIsClosed[i]:
				return False
		return True
	for chest in range(N):
		for key in keySet:
			if chestKeyType[chest] == key and currentKeys[key] > 0 and chestIsClosed[chest]: 
				# open next chest
				chestIsClosed[chest] = False
				currentKeys[key] -= 1
				stack.append(chest)
				for key2 in chestContents[chest]:
					currentKeys[key2] += chestContents[chest][key2]
				
				# next step
				ret = keySequenceHelper(N, currentKeys, keySet, chestKeyType, chestContents, step+1, chestIsClosed, stack)
				if ret:
					return True
				# close the chest
				chestIsClosed[chest] = True
				currentKeys[key] += 1
				stack.pop()
				for key2 in chestContents[chest]:
					currentKeys[key2] -= chestContents[chest][key2]	

if __name__ == "__main__":
	# main program
	full_path = os.path.realpath(__file__)
	path, file = os.path.split(full_path)

	f = open(path + '\\' + 'D-small-attempt0.in')
	numOfTests = int(f.readline())

	testData = []
	for currentTest in range(1,numOfTests+1):
		K, N = [int(x) for x in f.readline().split()] # read a line
		startKeys = [int(x) for x in f.readline().split()] # start keys
		chestKeyType = [None for x in range(N)]
		chestContents = []
		for i in range(N):
			buffer = []
			buffer = [int(x) for x in f.readline().split()]
			chestKeyType[i] = buffer[0]
			dict = {}
			for j in range(buffer[1]):
				if buffer[j+2] in dict:
					dict[buffer[j+2]] += 1
				else:
					dict[buffer[j+2]] = 1
			chestContents.append(copy.deepcopy(dict))
		testData.append((K, N, copy.deepcopy(startKeys), copy.deepcopy(chestKeyType), copy.deepcopy(chestContents)))
			
	from multiprocessing import Pool
	pool = Pool(processes=6)
	for i in range(1):
		print testData[i]
		print keySequence(testData[i])	
	'''
	results = pool.map(keySequence, testData, 1)

	outFile = open(path + '\\' + 'output.txt', 'w')
	for i in range(0, len(results)):
		caseNumber = i+1
		if (results[i] != None):
			for j in range(len(results[i])):
				results[i][j] += 1
			s = ' '.join(str(v) for v in results[i])
			outFile.write("Case #%d: %s\n" % (caseNumber, s))
		else:
			outFile.write("Case #%d: %s\n" % (caseNumber, 'IMPOSSIBLE'))
'''