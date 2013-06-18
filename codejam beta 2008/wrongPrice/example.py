#!/usr/bin/python

def memoize(func):
  def wrapper(*args):
    if args not in results:
      results[args] = func(*args) 
    return results[args]
  return wrapper

@memoize
def solve(cur, greatest):
  try:
    (n, v) = (names[cur], values[cur])
  except IndexError:
    return []
  if greatest is not None and v < greatest:
    return [n] + solve(cur + 1, greatest)
  else:
    exl1 = sorted(solve(cur + 1, v))
    exl2 = sorted([n] + solve(cur + 1, greatest))
    if len(exl1) < len(exl2):
      return exl1
    elif len(exl2) < len(exl1):
      return exl2
    else:
      if exl1 < exl2:
        return exl1
      else:
        return exl2

fIn = open('input.txt')
N = int(fIn.readline())
for case in range(1, N + 1):
  results = {}
  names = fIn.readline().split()
  values = [int(v) for v in fIn.readline().split()]
  print('Case #%d: %s' % (case, ' '.join(solve(0, -1))))