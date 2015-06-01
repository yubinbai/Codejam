import pstats
import sys
sys.stdout = open('stats.txt','w')
p = pstats.Stats('pstat.dat')
p.sort_stats('cumulative').print_stats(10)


