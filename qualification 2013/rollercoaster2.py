#roller coaster problem in 2010 google code jam
import collections, copy
def makeRide(group, K, N, start, result):
	if N==1:
		result.append(0)
		result.append(0)
		result.append(group[0])
		return

	currSum = 0
	curr = start
	while currSum + group[curr] <= K:
		currSum += group[curr]
		curr += 1
		if curr == N:
			curr = 0
		if curr == start:
			break

	result.append(start)
	result.append(curr)
	result.append(currSum)


def profits(R, K, N, group):

	prevRides = []
         
	totalProfit = 0
	remainingRides = R
	start = 0
	while remainingRides > 0:
		ride = []
		makeRide(group, K, N, start, ride)

		foundRide = -1
		for i in range(len(prevRides)):
			if str(prevRides[i]) == str(ride):
				foundRide = i
		
		if foundRide == -1:
			prevRides.append(copy.deepcopy(ride))
			totalProfit += ride[2]
			remainingRides -= 1
			start = ride[1]
		else:
			repeatProfit = 0
			for i in range(foundRide, len(prevRides)):
				repeatProfit += prevRides[i][2]
			repeatLength = len(prevRides)-foundRide
			numRepeats = remainingRides // repeatLength
			if numRepeats == 0:
				prevRides.append(copy.deepcopy(ride))
				totalProfit += ride[2]
				remainingRides -= 1
				start = ride[1]
				continue

			totalProfit += numRepeats * repeatProfit
			remainingRides -= numRepeats * repeatLength
			start = prevRides[-1][1]

	return totalProfit

if __name__ == '__main__':
	f = open('C-large-practice.in')

	numOfTests = int(f.readline())

	results = []
	for t in range(numOfTests):
		R, K, N = [int(x) for x in f.readline().split()]

		group = [int(x) for x in f.readline().split()]

		results.append(profits(R, K, N, group))

	o = open('output.txt','w')

	for i in range(numOfTests):
		o.write("Case #%d: %d\n" % (i+1, results[i]))