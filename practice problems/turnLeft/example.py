#!/usr/bin/python


(NORTH, SOUTH, WEST, EAST) = (1, 2, 4, 8)

LEFT = {NORTH: WEST,
        EAST: NORTH,
        SOUTH: EAST,
        WEST: SOUTH,
       }

RIGHT = {NORTH: EAST,
         EAST: SOUTH,
         SOUTH: WEST,
         WEST: NORTH,
        }

OPPOSITE = {NORTH: SOUTH,
            EAST: WEST,
            SOUTH: NORTH,
            WEST: EAST,
           }

MOVE = {NORTH: (0, 1),
        EAST: (1, 0),
        SOUTH: (0, -1),
        WEST: (-1, 0),
       }

OUTPUT = '0123456789abcdef'
fIn = open('input.txt')
N = int(fIn.readline())
for case in xrange(1, N + 1):
	maze = {}
	d = SOUTH
	(x, y) = (0, 0)
	maze[(x, y)] = 15 
	(mx, my, Mx, My) = (0, 0, 0, 0)
	for path in fIn.readline().split():
		old = 'W'
		for step in path[1:]:
		  if step == 'R':
		    if old == 'W':
		      # block left
		      maze[(x, y)] -= LEFT[d]
		    # block front
		    maze[(x, y)] -= d
		    d = RIGHT[d]
		  elif step == 'W':
		    if old == 'W':
		      # block left
		      maze[(x, y)] -= LEFT[d]
		    (x, y) = map(lambda (a, b): a + b, zip((x, y), MOVE[d]))
		    if (x, y) not in maze:
		      maze[(x, y)] = 15
		      if x < mx:
		        mx = x
		      elif x > Mx:
		        Mx = x
		      if y < my:
		        my = y
		      elif y > My:
		        My = y
		  elif step == 'L':
		    d = LEFT[d]
		  old = step
		del(maze[(x, y)])
		d = OPPOSITE[d]
		(x, y) = map(lambda (a, b): a + b, zip((x, y), MOVE[d]))

	print 'Case #%d:' % case
	for y in xrange(My, my - 1, -1):
		r = ''
		for x in xrange(mx, Mx + 1):
		  try:
		    r += OUTPUT[maze[(x, y)]]
		  except KeyError:
		    pass
		if r:
		  print r