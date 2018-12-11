import sys
import string
import numpy as np

np.set_printoptions(threshold=np.inf)

def Import_Data(path):
	f = open(path, 'r')
	return f.read().strip().split('\n')

def Clean_Data(rawdata):
	outvec = []
	for i in rawdata:
		i = i.replace('position=<','')
		i = i.replace('> velocity=<',' ').replace(',','').replace('>','')
		vals = i.split(' ')
		tmp = []
		for k in vals:
			if k is not '':
				tmp.append(int(k))
		outvec.append(tmp)
	return np.array(outvec)

def Find_Min(coords, it):
	coords[:,0] += it*coords[:,2]
	coords[:,1] += it*coords[:,3]

	# Shift to 0,0 for first particle
	xmin = min(coords[:,0])
	ymin = min(coords[:,1])
	coords[:,0] += -xmin
	coords[:,1] += -ymin

	xmax = max(coords[:,0])
	ymax = max(coords[:,1])

	return xmax, ymax, coords


def main():
	path = sys.argv[1]
	coords = Import_Data(path)
	coords = Clean_Data(coords)

	print(coords)

	lastmin = 999999
	tochk = -1
	for i in range(0,10):
		xmax, ymax, tempcoords = Find_Min(coords, i)
		print(i)
		if (xmax + ymax) > lastmin:
			tochk = i - 1
		else:
			lastmin = xmax + ymax

	xm, ym, coords = Find_Min(coords, tochk)

	print(coords)

if __name__ == '__main__':
	main()
	exit(0)