'''
Created on 2013-6-7

@author: Yubin Bai
'''
import time
from heapq import heappop, heappush

infinity = 1 << 32

def solve(T, tripsa, tripsb):
    trips = []
    for trip in tripsa:
        trips.append([trip[0], trip[1], 0])
    for trip in tripsb:
        trips.append([trip[0], trip[1], 1])
    trips.sort()

    start = [0, 0]
    trains = [[], []]

    for trip in trips:
        d = trip[2]
        if trains[d] and trains[d][0] <= trip[0]:
            # We're using the earliest train available, and
            # we have to delete it from this station's trains.
            heappop(trains[d])
        else:
            # No train was available for the current trip,
            # so we're adding one.
            start[d] += 1
        # We add an available train in the arriving station at the
        # time of arrival plus the turn-around time.
        heappush(trains[1 - d], trip[1] + T)
    return '%d %d' % (start[0], start[1])

if __name__ == '__main__':
    fIn = open('input.txt')
    fOut = open('output.txt', 'w')
    numOfTests = int(fIn.readline())
    
    millis1 = int(round(time.time() * 1000))
    
    for t in range(numOfTests):
        T = int(fIn.readline().strip())
        NA, NB = map(int, fIn.readline().strip().split())
        tripsa = []
        for i in range(NA):
            a, b = fIn.readline().strip().split()
            a = map(int, a.split(':'))
            b = map(int, b.split(':'))
            ab = [a[0] * 60 + a[1], b[0] * 60 + b[1]]
            tripsa.append(list(ab))
        tripsb = []
        for i in range(NB):
            a, b = fIn.readline().strip().split()
            a = map(int, a.split(':'))
            b = map(int, b.split(':'))
            ab = [a[0] * 60 + a[1], b[0] * 60 + b[1]]
            tripsb.append(list(ab))
        result = solve(T, tripsa, tripsb)
        fOut.write("Case #%d: %s \n" % (t + 1, result))
    
    millis2 = int(round(time.time() * 1000))
    print("Time in milliseconds: %d " % (millis2 - millis1))

    fIn.close()
    fOut.close()
