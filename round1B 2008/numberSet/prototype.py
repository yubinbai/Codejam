'''
Created on 2013-6-7

@author: Yubin Bai
'''

if __name__ == '__main__':
    N = 1000000
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    results = []
    for i in range(2, N):
        if sieve[i] == True:
            results.append(i)
            for j in range(i * 2, N, i):
                sieve[j] = False
    print(len(results))