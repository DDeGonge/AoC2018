import sys
import string
import numpy as np

np.set_printoptions(threshold=np.inf)

def Import_Data(path):
	f = open(path, 'r')
	return f.read().strip()

def Gen_Grid(val):
	pl = np.zeros((300,300))
	for x in range(0, 300):
		for y in range(0, 300):
			rid = x + 10
			tmp = ((rid * y) + val) * rid
			pl[x,y] = (tmp // 100)%10 - 5
	return pl

def Find_Max(pl, s):
	maxsum = -100
	maxpos = (-1,-1)
	for x in range(0, 301 - s):
		for y in range(0, 301 - s):
			if np.sum(pl[x:x+s,y:y+s]) > maxsum:
				maxsum = np.sum(pl[x:x+s,y:y+s])
				maxpos = (x,y)
	return maxsum, maxpos

def main():
	#path = sys.argv[1]
	val = 6303
	pl = Gen_Grid(val)

	maxsize = -1
	gmaxsum = -1
	gmaxpos = (-1,-1)
	for i in range(1, 299):
		print(i)
		thissum, thispos = Find_Max(pl, i)
		if thissum > gmaxsum:
			gmaxsum = thissum
			gmaxpos = thispos
			maxsize = i

	print(maxsize)
	print(gmaxpos)
	

if __name__ == '__main__':
	main()
	exit(0)