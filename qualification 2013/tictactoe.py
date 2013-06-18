'''
Solving the first code jam problem

'''
import threading
class SolvingThread(threading.Thread):
	def __init__(self, matrix):
		threading.Thread.__init__(self)
		self.matrix = matrix
		self.result = None
		
	def run(self):
		xrow = [0,0,0,0]
		xcol = [0,0,0,0]
		xdiag = 0
		xantiDiag = 0
		orow = [0,0,0,0]
		ocol = [0,0,0,0]
		odiag = 0
		oantiDiag = 0

		blanks = 0
		for i in range(4):
			for j in range(4):
				if self.matrix[i][j] == 'X':
					xrow[i] += 1;
					xcol[j] += 1;
				elif self.matrix[i][j] == 'O':
					orow[i] += 1;
					ocol[j] += 1;
				elif self.matrix[i][j] == '.':
					blanks += 1
				else:
					#the site is T
					xrow[i] += 1;
					xcol[j] += 1;
					orow[i] += 1;
					ocol[j] += 1;
		for i in range(4):
			if self.matrix[i][i] == 'X':
				xdiag += 1;
			elif self.matrix[i][i] == 'O':
				odiag += 1
			else:
				pass #the site is T
				
			if self.matrix[i][3-i] == 'X':
				xantiDiag += 1;
			elif self.matrix[i][3-i] == 'O':
				oantiDiag += 1
			else:
				pass #the site is T
		for x in xrow:
			if x == 4:
				self.result = 1
				return # X won
		for x in xcol:
			if x == 4:
				self.result = 1
				return # X won
		for x in xdiag,xantiDiag:
			if x == 4:
				self.result = 1
				return # X won
		for x in orow:		
			if x == 4:
				self.result = -1
				return # O won	
		for x in ocol:		
			if x == 4:
				self.result = -1
				return # O won
		for x in odiag,oantiDiag:
			if x == 4:
				self.result = -1
				return # O won
				
		if (blanks == 0):
			self.result = 0 # draw
		else:
			self.result = 9999 # game not complete
# main program
import os
full_path = os.path.realpath(__file__)
path, file = os.path.split(full_path)

f = open(path + '\\' + 'A-large.in')
numOfTests = int(f.readline())


threads = []

for currentTest in range(1,numOfTests+1):
	data = []
	
	for line in range(4):
		thisLine = list(f.readline())
		data.append(thisLine)
	f.readline()
	
	import copy
	thread1 = SolvingThread(copy.deepcopy(data))
	threads.append(thread1)

for t in threads:
	t.start()
	
for t in threads:
	t.join()

outFile = open(path + '\\' + 'output.txt', 'w')
for i in range(0, len(threads)):
	caseNumber = i+1
	if threads[i].result == 1:
		outFile.write("Case #%d: X won\n" % caseNumber )
	elif threads[i].result == -1:
		outFile.write("Case #%d: O won\n" % caseNumber )
	elif threads[i].result == 0:
		outFile.write("Case #%d: Draw\n" % caseNumber )
	else:
		outFile.write("Case #%d: Game has not completed\n" % caseNumber )