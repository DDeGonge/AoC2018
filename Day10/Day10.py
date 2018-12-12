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

def Get_Min(cin):
	tc = cin
	tc[:,0] += tc[:,2]
	tc[:,1] += tc[:,3]

	# Shift to 0,0 for first particle
	xmin = min(tc[:,0])
	ymin = min(tc[:,1])
	tc[:,0] += -xmin
	tc[:,1] += -ymin

	xmax = max(tc[:,0])
	ymax = max(tc[:,1])

	return xmax, ymax

def Transform_Plt(cin, it):
	coords = cin
	coords[:,0] += it*coords[:,2]
	coords[:,1] += it*coords[:,3]

	# Shift to 0,0 for first particle
	xmin = min(coords[:,0])
	ymin = min(coords[:,1])
	coords[:,0] += -xmin
	coords[:,1] += -ymin

	return coords

def Plot_Points(cin):
	try:
		ymax = max(cin[:,0]) + 1
		xmax = max(cin[:,1]) + 1

		ar = np.zeros((xmax, ymax))
		ar += 1
		for p in cin:
			ar[p[1], p[0]] = 0
		print(ar)
		for i in ar:
			line = ''
			for l in i:
				if l == 0:
					line += '#'
				else:
					line += '_'
			print(line)
	except:
		pass


def main():
	path = sys.argv[1]
	coords = Import_Data(path)
	coords = Clean_Data(coords)

	print(coords)

	lastmin = 999999
	tochk = -1
	for i in range(0,1000000):
		xmax, ymax = Get_Min(coords)
		print(i, xmax, ymax)
		if (xmax + ymax) > lastmin:
			tochk = i# - 1
			break
		else:
			lastmin = xmax + ymax

	coords = Import_Data(path)
	coords = Clean_Data(coords)
	coords = Transform_Plt(coords, tochk)
	Plot_Points(coords)

	#print(coords, xm, ym)

if __name__ == '__main__':
	main()
	exit(0)