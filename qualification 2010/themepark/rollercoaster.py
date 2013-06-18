#roller coaster problem in 2010 google code jam
import collections
class queueWithSum:
	data = collections.deque()
	total = 0

	def enqueue(self, e):
		self.total += e
		self.data.append(e)

	def dequeue(self):
		self.total -= self.data[0]
		return self.data.popleft()

	def getSum(self):
		return self.total

	def isEmpty(self):
		return len(self.data) == 0


def profits(R, K, group):

	queue = collections.deque(group)
	currentRide = queueWithSum()

	totalProfit = 0
	remainingRides = R
	currPos = 0
	while remainingRides > 0:
		while len(queue) > 0 and currentRide.getSum() + queue[0] <= K:
			currentRide.enqueue(queue.popleft()) 
		totalProfit += currentRide.getSum()
		while not currentRide.isEmpty():
			queue.append(currentRide.dequeue())

		remainingRides -= 1
	return totalProfit



if __name__ == '__main__':
	f = open('C-large-practice.in')

	numOfTests = int(f.readline())

	results = []
	for t in range(numOfTests):
		R, K, N = [int(x) for x in f.readline().split()]

		group = [int(x) for x in f.readline().split()]

		results.append(profits(R, K, group))

	o = open('output.txt','w')

	for i in range(numOfTests):
		o.write("Case #%d: %d\n" % (i+1, results[i]))