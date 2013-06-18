#snapper problem in 2010 google code jam

def  isON(N, K):
	number = (1 << N) - 1
	if K % (1 << N) == number:
		return 'ON'
	else:
		return 'OFF'



if __name__ == '__main__':
	f = open('A-large-practice.in')

	numOfTests = int(f.readline())

	results = []
	for t in range(numOfTests):
		N, K = [int(x) for x in f.readline().split()]

		results.append(isON(N, K))

	o = open('output.txt','w')

	for i in range(numOfTests):
		o.write("Case #%d: %s\n" % (i+1, results[i]))